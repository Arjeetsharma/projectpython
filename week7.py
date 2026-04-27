def filter_heavy_orders(orders, threshold):
    return [order for order in orders if order['weight'] > threshold]

orders = [
    {"id": "O1", "weight": 5},
    {"id": "O2", "weight": 3},
    {"id": "O3", "weight": 8}
]

heavy = filter_heavy_orders(orders, 4)
for order in heavy:
    print(f"Heavy Order: {order['id']}, Weight: {order['weight']}kg")
