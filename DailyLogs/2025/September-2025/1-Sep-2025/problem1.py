# Prints the Coin with the Max Price

coins = {
    "BTC": {"price": 60000, "rank": 1},
    "ETH": {"price": 3000, "rank": 2},
    "SOL": {"price": 150, "rank": 6},
}

coin_prices = []

for info in coins.values():  # loop over the price and make a list
    prices = info["price"]
    coin_prices.append(prices)

max_coin_prices = max(coin_prices)  # find max price

for coin, info in coins.items():  # price coin with the max price
    if info["price"] == max_coin_prices:
        print(f"{coin}: {info}")
