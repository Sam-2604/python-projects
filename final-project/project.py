import requests, csv

def main():
    # 1. Ask for preferences
    want_data = input("Generate machine-readable data report? (y/n): ").lower() == 'y'
    want_user = input("Generate user-friendly report? (y/n): ").lower() == 'y'
    want_med = input("Include Medicine Info? (y/n): ").lower() == 'y'
    want_caution = input("Include Caution Info? (y/n): ").lower() == 'y'

    # 2. Collect medicines
    user_medicines = get_drug_name()

    if want_data:
        with open("data_report.csv", "w", newline="") as f:
            csv.writer(f).writerow(["Medicine Name", "Category", "Attribute", "Details"])

    # 3. Processing Loop
    for med in user_medicines:
        try:
            drug_info = fetch_drug_info(med)
            med_info, caution_info = parse_med_data(drug_info, med)
            # 4. Pass flags to the save function
            save_to_csv(med, med_info, caution_info, want_data, want_user, want_med, want_caution)

        except (ValueError, ConnectionError) as e:
            print(e)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def get_drug_name():
    # This function will prompt the user to provide an input
    medicines = []
    while True:
        names = input("Enter name of medicine(s) or ('q' to quit): ").strip()
        if not any(char.isalnum() for char in names):
            raise ValueError("Invalid Input")
        if names.lower() == "q":
            break
        medicines.append(names)
    return medicines

def fetch_drug_info(name):
    # This function will use the user input and call an API to return data in JSON format

    # Base URL for the openFDA API
    url = "https://api.fda.gov/drug/label.json"

    params = {"search": f"openfda.brand_name:{name}"}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 404:
            raise ValueError(f"Medicine '{name}' not found in the FDA database.")

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        raise ConnectionError("Unable to connect to the FDA API. Please check your internet.")

def parse_med_data(json_response, requested_name):
    # This function will go through the data that the API returned and filter and return what we want
    results = json_response.get("results", [])
    if not results:
        raise ValueError("No data found.")

    for result in results:
        brand_names = result.get("openfda", {}).get("brand_name", [])

        if any(requested_name.lower() in name.lower() for name in brand_names):
            return extract_data(result)

    raise ValueError(f"No specific data found for '{requested_name}'.")


def extract_data(result):
    # Extracting into groups
    medicine_info = {
        "brand_name": result.get("openfda", {}).get("brand_name", ["N/A"])[0],
        "generic_name": result.get("openfda", {}).get("generic_name", ["N/A"])[0],
        "route": result.get("openfda", {}).get("route", ["N/A"])[0],
        "product_type": result.get("openfda", {}).get("product_type", ["N/A"])[0],
        "active_ingredient": result.get("active_ingredient", ["N/A"]),
        "purpose": result.get("purpose", ["N/A"]),
        "indications": result.get("indications_and_usage", ["N/A"])
    }

    caution_info = {
        "warnings": result.get("warnings", ["N/A"]),
        "do_not_use": result.get("do_not_use", ["N/A"]),
        "ask_doctor": result.get("ask_doctor", ["N/A"]),
        "ask_doctor_or_pharmacist": result.get("ask_doctor_or_pharmacist", ["N/A"]),
        "stop_use": result.get("stop_use", ["N/A"]),
        "pregnancy_or_breast_feeding": result.get("pregnancy_or_breast_feeding", ["N/A"]),
        "other_safety_information": result.get("other_safety_information", ["N/A"])
    }

    return medicine_info, caution_info

def clean_value(value):
    # To clean up a specific data bug found
    if isinstance(value, list):
        return "; ".join(map(str, value)).replace("Purpose", "").replace(":", "").strip()
    return str(value).replace("Purpose", "").replace(":", "").strip()

def save_to_csv(med, med_info, caution_info, data, user, want_med, want_caution):
    if data:
        # 1. The Machine-Readable Version (Nnarrow format)
        with open("data_report.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if want_med:
                for k, v in med_info.items():
                    writer.writerow([med, "Medicine Info", k, clean_value(v)])
            if want_caution:
                for k, v in caution_info.items():
                    writer.writerow([med, "Caution Info", k, clean_value(v)])

    if user:
        # 2. The Human-Readable Version (Vertical Block Format)
        with open("user_report.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Clear separator for each medicine
            writer.writerow(["="*20])
            writer.writerow(["MEDICINE:", med])
            writer.writerow(["="*20])

            if want_med:
                writer.writerow(["--- MEDICINE INFO ---"])
                for key, val in med_info.items():
                    writer.writerow([key.replace("_", " ").title(), clean_value(val)])

            writer.writerow([]) # Empty row for spacing

            if want_caution:
                writer.writerow(["--- CAUTION INFO ---"])
                for key, val in caution_info.items():
                    writer.writerow([key.replace("_", " ").title(), clean_value(val)])

            writer.writerow([]) # Empty row for spacing

    print(f"Success! Report(s) saved for {med}")


if __name__ == "__main__":
    main()
