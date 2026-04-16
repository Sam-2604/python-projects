# Then in a separate main.py, import those functions and
# build a simple currency converter that asks the user which conversion they want and the amount.

from converter import usd_to_inr, inr_to_usd


def main():
    input_str = input("Enter conversion type (1 for USD to INR, 2 for INR to USD): ")
    amount = float(input("Enter the amount to convert: "))
    if input_str == "1":
        result = usd_to_inr(amount)
        print(f"{amount} USD is equal to {result} INR.")
    elif input_str == "2":
        result = inr_to_usd(amount)
        print(f"{amount} INR is equal to {result} USD.")
    else:
        print("Invalid conversion type. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
