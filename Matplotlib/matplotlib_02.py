import matplotlib.pyplot as plt

x = [1, 2, 3] # "x" is the horizontal axis
y = [10, 30, 50] # "y" is the vertical axis

x2 = [1, 2, 3]

y2 = [10, 31, 52]

plt.plot(x, y, label="First Line = American Consumerism") # "plot" is the informations

plt.plot(x2, y2, label="Second Line = Brazilian Consumerism")

plt.title("Brazilian Consumism and\nAmerican Consumism (%)")

plt.xlabel("Years")

plt.ylabel("Pourcent")

plt.legend()

plt.show() # "show" show the graph 
