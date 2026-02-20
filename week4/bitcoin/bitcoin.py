import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=4777ab20155abd9f1818a81a3354ee1a637d205974dfcba123421ba909b7b805"
        ).json()
        price = float(response["data"]["priceUsd"])
        print(f"${price*number:,.4f}")
    except requests.RequestException:
        sys.exit(1)
    except [KeyError, ValueError]:
        sys.exit(1)


main()
