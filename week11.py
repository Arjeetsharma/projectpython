def track_delivery(order_id, status):
    statuses = {
        "pending": "Order Pending",
        "shipped": "Order Shipped",
        "delivered": "Order Delivered"
    }
    return statuses.get(status, "Unknown Status")

print(track_delivery("O1", "shipped"))
