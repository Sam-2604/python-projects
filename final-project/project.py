import requests, csv, sys

class Medicine:
    def __init__(self, name, api_result):
        self.name = name
        # Using data extraction inside the class
        self.med_info = {
            "Brand Name": api_result.get("openfda", {}).get("brand_name", ["N/A"])[0],
            "Generic Name": api_result.get("openfda", {}).get("generic_name", ["N/A"])[0],
            "Route": api_result.get("openfda", {}).get("route", ["N/A"])[0],
            "Product Type": api_result.get("openfda", {}).get("product_type", ["N/A"])[0],
            "Active Ingredient": self._format_list(api_result.get("active_ingredient", [])),
            "Purpose": self._format_list(api_result.get("purpose", [])),
            "Indications": self._format_list(api_result.get("indications_and_usage", []))
        }

        self.caution_info = {
            "Warnings": self._format_list(api_result.get("warnings", [])) or api_result.get("warnings_and_cautions", []) or api_result.get("boxed_warning", []),
            "Do Not Use": self._format_list(api_result.get("do_not_use", [])),
            "Ask Doctor": self._format_list(api_result.get("ask_doctor", [])),
            "Pregnancy": self._format_list(api_result.get("pregnancy_or_breast_feeding", [])),
            "Stop Use": self._format_list(api_result.get("stop_use", []))
        }

    def _format_list(self, value_list):
        # To convert details which are returns as a list to str for displaying output
        if not value_list:
            return "N/A"
        # Joining with newlines for the User Report
        text = " ".join(map(str, value_list))
        # Removing certain inconsistencies in the output
        return text.replace("Purpose", "").replace("Warnings", "").replace(":", "").strip().replace("INDICATIONS AND USAGE", "")

    def __str__(self):
        return f"Medicine Object: {self.name} ({self.med_info['Brand Name']})"


def main():
    # 1. Disclaimer and Info
    print_welcome()

    # 2. Ask for preferences
    want_data = input("Generate data report? (y/n): ").lower() == 'y'
    want_user = input("Generate user report? (y/n): ").lower() == 'y'
    want_med = input("Include Medicine Info? (y/n): ").lower() == 'y'
    want_caution = input("Include Caution Info? (y/n): ").lower() == 'y'

    # Exit Failsafe
    if not (want_med or want_caution):
        sys.exit("No information selected to save. Exiting program.")

    # 3. Collect medicines
    user_medicines = get_drug_names()

    # 4. Initialize output files
    if want_data:
        with open("data_report.csv", "w", newline="") as f:
            csv.writer(f).writerow(["Medicine Name", "Category", "Attribute", "Details"])
    if want_user:
        with open("user_report.csv", "w", newline="") as f:
            f.write("MEDICATION GUIDE - USER REPORT\n" + "="*30 + "\n")

    # 5. Processing Loop (Main Program)
    for med_name in user_medicines:
        try:
            raw_data = fetch_drug_info(med_name)
            # Data Validation to prevent misinformation
            valid_result = validate_result(raw_data, med_name)

            # Creates the Class Object
            current_med = Medicine(med_name, valid_result)

            # 6. Output Preparation
            save_reports(current_med, want_data, want_user, want_med, want_caution)
            print(f"✅ Processed {med_name}")

        except ValueError as e:
            print(f"❌ Skipping {med_name}: {e}")
        except ConnectionError as e:
            print(f"🌐 Connection issue: {e}")


def print_welcome():

    print("\n" + "="*50)
    print("             🌟 Medication Guide 🌟")
    print("="*50)

    print("\n[ PURPOSE ]")
    print("Fetches key details for medicines via the openFDA API.")

    print("\n[ INSTRUCTIONS ]")
    print("1. Set your preferences for report types (Data vs. User).")
    print("2. Choose categories (Primary Info vs. Cautions).")
    print("3. Enter medicine names (Type 'q' to finish).")
    print("   *Answer all prompts with 'y' (yes) or 'n' (no).")

    print("\n" + "!"*50)
    print("🚨 MEDICAL DISCLAIMER 🚨")
    print("This tool is for informational purposes only.")
    print("It is based on U.S. FDA data and is NOT medical advice.")
    print("ALWAYS consult a doctor or pharmacist before taking action.")
    print("!"*50 + "\n")


def get_drug_names():
    medicines = []
    print("Enter medicine names (type 'q' to finish):")
    while True:
        name = input("> ").strip()
        if name.lower() == "q":
            break
        if not any(char.isalnum() for char in name):
            print("Invalid Input: Please enter a valid medicine name.")
            continue  # Reprompts user for input
        medicines.append(name)
    return medicines


def fetch_drug_info(name):
    url = "https://api.fda.gov/drug/label.json" # Main API URL
    params = {"search": f"openfda.brand_name:{name}"} # To join the URL and medicine name
    try:
        response = requests.get(url, params=params)
        if response.status_code == 404: # 404 = Server could not find the requested page or source
            raise ValueError("Not found in FDA database.")
        response.raise_for_status() # API Failsafe
        return response.json()
    except requests.exceptions.RequestException:
        raise ConnectionError("FDA API unreachable.")


def validate_result(json_response, requested_name):
    # This function performs data validation to ensure prevention of misinformation
    results = json_response.get("results", [])
    for result in results:
        brands = result.get("openfda", {}).get("brand_name", [])
        if any(requested_name.lower() in b.lower() for b in brands):
            return result
    raise ValueError("No specific brand match found.")


def save_reports(med_obj, do_data, do_user, inc_med, inc_caution):
    if do_data:
        # Machine-Readable CSV File (Narrow Format)
        with open("data_report.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if inc_med:
                for k, v in med_obj.med_info.items():
                    writer.writerow([med_obj.name, "Medicine Info", k, v])
            if inc_caution:
                for k, v in med_obj.caution_info.items():
                    writer.writerow([med_obj.name, "Caution Info", k, v])

    if do_user:
        # User-Friendly CSV File (Vertical Long Format)
        with open("user_report.csv", "a") as f:
            f.write(f"\nMEDICINE: {med_obj.name.upper()}\n" + "-"*20 + "\n")
            if inc_med:
                f.write("[ MEDICINE INFO ]\n")
                for k, v in med_obj.med_info.items():
                    f.write(f"{k}: {v}\n")
            if inc_caution:
                f.write("\n[ CAUTION & WARNINGS ]\n")
                for k, v in med_obj.caution_info.items():
                    f.write(f"{k}: {v}\n")
            f.write("\n" + "="*30 + "\n")


if __name__ == "__main__":
    main()
