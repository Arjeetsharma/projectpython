import json

order_data = {
    "orders": [
        {"id": "O1", "weight": 5},
        {"id": "O2", "weight": 3},
        {"id": "O3", "weight": 7}
    ]
}

json_string = json.dumps(order_data, indent=2)
print(json_string)
