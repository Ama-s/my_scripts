import sys
import requests
import json

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        bitcoin = float(sys.argv[1])

except (ValueError):
    sys.exit("Command-line argument is not a number")

try:
    #gets the json api from the internet, it's open source
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(response.json(), indent=4))

    # saves that json file in my own variable
    bitcoin_obj = response.json()

    #to access a value that's a dictionary and has its own keys in it
    rate = bitcoin_obj["bpi"]["USD"]["rate_float"]

    total_cost = bitcoin * rate

    #to format a whole number by adding commas and at the same time, approximate the decimal to 4dp
    print("$"f"{total_cost:,.4f}")

except requests.RequestException:
    sys.exit()