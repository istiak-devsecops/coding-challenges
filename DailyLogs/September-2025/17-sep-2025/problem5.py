# Create a shopping cart that adds items and sums their quantities automatically.
from collections import defaultdict

# Nested defaultdict: user → item → quantity
shopping_carts = defaultdict(lambda: defaultdict(int))

# Simulated purchases
purchases = [
    ("user1", "apple"),
    ("user1", "banana"),
    ("user1", "apple"),
    ("user2", "orange"),
    ("user2", "orange"),
    ("user2", "orange")
]

# Track items per user
for user, item in purchases:
    shopping_carts[user][item] += 1

# Print results
for user, cart in shopping_carts.items():
    print(f"{user}'s cart:")
    for item, qty in cart.items():
        print(f"  {item}: {qty}")
