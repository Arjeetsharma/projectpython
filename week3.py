# Basic sorting of orders
orders = [
    {"id": "O3", "weight": 7},
    {"id": "O1", "weight": 5},
    {"id": "O2", "weight": 3}
]

sorted_orders = sorted(orders, key=lambda x: x['weight'])
for order in sorted_orders:
    print(f"Order {order['id']}: {order['weight']}kg")
