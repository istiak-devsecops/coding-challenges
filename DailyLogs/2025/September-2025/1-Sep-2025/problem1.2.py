# Prints the Coin with the Max Price

coins = {
    "BTC": {"price": 60000, "rank": 1},
    "ETH": {"price": 3000, "rank": 2},
    "SOL": {"price": 150, "rank": 6},
}


max_coin_price = float("-inf")  # Start with the lowest price
max_coin_name = ""

for coin, info in coins.items():  # loop through the keys and values to find the max
    price = info["price"]
    if price > max_coin_price:
        max_coin_price = price
        max_coin_name = coin

print(f"Highest priced coin: {max_coin_name} at ${max_coin_price}")
