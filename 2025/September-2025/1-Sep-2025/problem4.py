# Reverse dict

cryptos = {"BTC": 60000, "ETH": 3000}
reverse_cryptos = {}

for coin, price in cryptos.items():
    reverse_cryptos[price] = coin


print(reverse_cryptos)
