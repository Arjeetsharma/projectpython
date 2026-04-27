transport_requests = [
    {"customer": "Alice", "order_id": "O1", "weight": 5},
    {"customer": "Bob", "order_id": "O2", "weight": 3},
    {"customer": "Charlie", "order_id": "O3", "weight": 7}
]

for request in transport_requests:
    print(f"Customer: {request['customer']}, Order: {request['order_id']}, Weight: {request['weight']}kg")
