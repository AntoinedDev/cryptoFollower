import time
import json
import requests
from colorama import Fore, Style

class FollowTheMoney():
    def __init__(self, crypto):
        self.crypto = crypto

    def get_the_price(self):
        response = requests.get('https://api.coinbase.com/v2/prices/{}-EUR/spot'.format(self.crypto))
        data = json.dumps(response.json())
        price = data[55:-3]
        print("{} price currently is: ".format(self.crypto)+Fore.GREEN+"{}".format(price)+Style.RESET_ALL)


def money():
    while True:
        ethereum = FollowTheMoney("ETH")
        bitcoin = FollowTheMoney("BTC")
        print("----------------------------")
        ethereum.get_the_price()
        bitcoin.get_the_price()
        time.sleep(30)
money()
