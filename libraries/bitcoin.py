# Makes an API call to https://api.coindesk.com/v1/bpi/currentprice.json using requests,
# parses the JSON response,
# and prints the current Bitcoin price in USD formatted to 2 decimal places.
# Handle the case where the request fails.

import requests


def main():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        price = data["bitcoin"]["usd"]
        print(f"Current Bitcoin price in USD: ${price:.2f}")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.RequestException as req_err:
        print(f"Request error occurred: {req_err}")


if __name__ == "__main__":
    main()
