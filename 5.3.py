import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

# line plot
# plt.plot(year, pop)

# fill_between command
plt.fill_between(year, pop, 0, color = 'green')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
    ['0', '2B', '4B','6B','8B','10B'])


plt.show()

# dict = {
#     'Asia':'red',
#     'Europe':'green',
#     'Africa':'blue',
#     'Americas':'yellow',
#     'Oceania':'black'
# }
# example of customization on scatter plot
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# plt.show()

# Additional customizations
# plt.text(1550, 71, 'India')
# plt.text(5700, 80, 'China')

# Add grid() call
# plt.grid(True)