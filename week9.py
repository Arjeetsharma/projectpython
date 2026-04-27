try:
    weight = float(input("Enter weight: "))
    if weight <= 0:
        raise ValueError("Weight must be positive")
    print(f"Valid weight: {weight}kg")
except ValueError as e:
    print(f"Error: {e}")
