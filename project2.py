
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line Graph
ax[0, 0].plot(x, [2, 4, 6, 8, 10])
ax[0, 0].set_title("Line Graph")
ax[0, 0].grid(True)
ax[0, 0].set_xlabel("X")
ax[0, 0].set_ylabel("Y")



# 2. Bar Graph
ax[0, 1].bar(x, [5, 8, 3, 7, 6])
ax[0, 1].set_title("Bar Graph")
ax[0, 1].grid(True)
ax[0, 1].set_xlabel("X")
ax[0, 1].set_ylabel("Y")

# 3. Scatter Graph
ax[1, 0].scatter(x, [3, 7, 2, 8, 5])
ax[1, 0].set_title("Scatter Graph")
ax[1, 0].grid(True)
ax[1, 0].set_xlabel("X")
ax[1, 0].set_ylabel("Y")


# 4. Pie Chart
ax[1, 1].pie([30, 25, 20, 25], labels=["A", "B", "C", "D"])
ax[1, 1].set_title("Pie Chart")



plt.tight_layout()
plt.show()