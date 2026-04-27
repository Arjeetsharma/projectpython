def calculate_delivery_cost(weight, distance):
    base_cost = 50
    per_kg = weight * 10
    per_km = distance * 5
    return base_cost + per_kg + per_km

weight = 5
distance = 10
cost = calculate_delivery_cost(weight, distance)
print(f"Delivery Cost: Rs. {cost}")
