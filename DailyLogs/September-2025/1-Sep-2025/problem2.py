#Merge Two Dicts with Sum

from collections import defaultdict

wallet1 = {"BTC": 1, "ETH": 5, "SOL": 10}
wallet2 = {"ETH": 3, "SOL": 5, "ADA": 20}

merged_wallet = defaultdict(int)

for coin, amount in wallet1.items():
    merged_wallet[coin] += amount

for coin, amount in wallet2.items():
    merged_wallet[coin] += amount

merged_wallet = dict(merged_wallet)

print(f"Total amount of coins: {merged_wallet}")




