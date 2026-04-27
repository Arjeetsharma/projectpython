class Transport:
    def __init__(self, order_id, weight):
        self.order_id = order_id
        self.weight = weight
    
    def get_info(self):
        return f"Order {self.order_id}: {self.weight}kg"

transport = Transport("O1", 5)
print(transport.get_info())
