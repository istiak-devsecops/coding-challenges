#Reverse cryptos using modules

cryptos = {"BTC": 60000, "ETH": 3000}

from collections import defaultdict
reverse_info = defaultdict(list)

for coin, price in cryptos.items():
    reverse_info[price].append(coin)

print(dict(reverse_info))