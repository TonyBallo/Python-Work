import pandas as pd
from matplotlib import pyplot as plt


"""
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

plt.plot(x,y)
plt.plot(x,z)

plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])

"""
data = pd.read_csv("countries.csv")

# Comparing the population growth in the US and China

us = data[data.country == 'United States']
china = data[data.country == 'China']

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

