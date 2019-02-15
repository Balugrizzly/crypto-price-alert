import requests
import json


alert_msg = """
 __    ____  ____  ___     ___  _____    __    ____  ____  ___     ___  _____
(  )  ( ___)(_  _)/ __)   / __)(  _  )  (  )  ( ___)(_  _)/ __)   / __)(  _  )
 )(__  )__)   )(  \__ \  ( (_-. )(_)(    )(__  )__)   )(  \__ \  ( (_-. )(_)(
(____)(____) (__) (___/   \___/(_____)  (____)(____) (__) (___/   \___/(_____)

"""


def get_coins():
    with open('config.json') as json_data:
        return json.load(json_data)["coins"]


coins = get_coins()
for coin in coins:
    ticker = coin["ticker"]
    payload = {'ids': ticker, 'vs_currencies': 'btc'}
    r = requests.get(
        'https://api.coingecko.com/api/v3/simple/price',
        params=payload)
    price = r.json()[ticker]["btc"]

    if coin["trigger"] == "above" and price > coin["price"]:
        print("{0} is {1} above your trigger point".format(ticker,
                                                           price - coin["price"]))

    if coin["trigger"] == "below" and price < coin["price"]:
        print("{0} is {1} below your trigger point".format(ticker,
                                                           coin["price"] - price))
