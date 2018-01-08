import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# line plot
# plt.plot(year, pop)
# plt.show()

# scatter plot
plt.scatter(year, pop)
plt.show()

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()