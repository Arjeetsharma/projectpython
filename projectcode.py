
import math 
from dataclasses import dataclass
 
# ----------------------------- 
# Data Models 
# ----------------------------- 
@dataclass 
class Order: 
    id: str 
    pickup: tuple 
    dropoff: tuple 
    weight: float 
    earliest: int 
    latest: int 
    service_time: int 
 
@dataclass 
class Vehicle: 
    id: str 
    capacity: float 
    start_location: tuple 
    route: list 
    load: float = 0 
 
# ----------------------------- 
# Global Lists 
# ----------------------------- 
orders = [] 
vehicles = [] 
 
# ----------------------------- 
# Distance Function 
# ----------------------------- 
def distance(loc1, loc2): 
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2) 
 
# ----------------------------- 
# Order Management 
# ----------------------------- 
def add_order(order): 
    orders.append(order) 
    print("Order added:", order.id) 
 
def remove_order(order_id): 
    global orders 
    orders = [o for o in orders if o.id != order_id] 
    print("Order removed:", order_id) 
 
# ----------------------------- 
# Vehicle Management 
# ----------------------------- 
def add_vehicle(vehicle): 
    vehicles.append(vehicle) 
    print("Vehicle added:", vehicle.id) 
 
# ----------------------------- 
# Route Optimization (Greedy) 
# ----------------------------- 
def route_optimization(): 
    print("\nRoute Optimization Started") 
 
    for order in orders: 
        best_vehicle = None 
        best_distance = float('inf') 
 
        for vehicle in vehicles: 
            if vehicle.load + order.weight <= vehicle.capacity: 
                if vehicle.route:  
                    last_location = vehicle.route[-1] 
                else: 
                    last_location = vehicle.start_location 
 
                d = distance(last_location, order.pickup) 
 
                if d < best_distance: 
                    best_distance = d 
                    best_vehicle = vehicle 
 
        if best_vehicle: 
            best_vehicle.route.append(order.pickup) 
            best_vehicle.route.append(order.dropoff) 
            best_vehicle.load += order.weight 
# ----------------------------- 
# Dynamic Re-Routing 
# ----------------------------- 
def dynamic_reroute(new_order): 
    print("\nDynamic Re-routing Started") 
 
    best_vehicle = None 
    best_distance = float('inf') 
 
    for vehicle in vehicles: 
        if vehicle.load + new_order.weight <= vehicle.capacity: 
            if vehicle.route: 
                last_location = vehicle.route[-1] 
            else: 
                last_location = vehicle.start_location 
 
            d = distance(last_location, new_order.pickup) 
 
            if d < best_distance: 
                best_distance = d 
                best_vehicle = vehicle 
 
    if best_vehicle: 
        best_vehicle.route.append(new_order.pickup) 
        best_vehicle.route.append(new_order.dropoff) 
        best_vehicle.load += new_order.weight 
        print(f"New Order {new_order.id} assigned to Vehicle {best_vehicle.id}") 
 
# ----------------------------- 
# Display Routes 
# ----------------------------- 
def display_routes(): 
    print("\nFinal Routes") 
    for vehicle in vehicles: 
        print("\nVehicle:", vehicle.id) 
        print("Route:", vehicle.route) 
        print("Load:", vehicle.load) 
 
# ----------------------------- 
# Main Program 
# ----------------------------- 
def main(): 
    # Add Vehicles 
    v1 = Vehicle("V1", 10, (0, 0), []) 
    v2 = Vehicle("V2", 15, (5, 5), []) 
    add_vehicle(v1) 
    add_vehicle(v2) 
 
    # Add Orders 
    o1 = Order("O1", (1, 2), (3, 4), 3, 9, 12, 5) 
    o2 = Order("O2", (6, 5), (7, 8), 4, 10, 14, 5) 
    o3 = Order("O3", (2, 1), (4, 3), 2, 11, 15, 5) 
 
    add_order(o1) 
    add_order(o2) 
    add_order(o3) 
 
    # Optimize Routes 
    route_optimization() 
 
    # Dynamic Order 
    new_order = Order("O4", (8, 8), (9, 9), 3, 12, 16, 5) 
    dynamic_reroute(new_order) 
 
    # Display Routes 
    display_routes() 

if __name__ == "__main__":
    main()
    main() 
