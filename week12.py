import matplotlib.pyplot as plt

orders = ["O1", "O2", "O3"]
weights = [5, 3, 7]

plt.bar(orders, weights)
plt.xlabel("Orders")
plt.ylabel("Weight")
plt.title("Order Weights")
plt.show()
