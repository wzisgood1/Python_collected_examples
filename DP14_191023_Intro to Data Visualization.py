# ********** ********** ********** **********
# import all libraries for this program
# ********** ********** ********** **********
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os.path
import os
from datetime import datetime

# ********** ********** ********** **********
# define input and output directories, and current date
# ********** ********** ********** **********
input_dir  = 'C:\\Users\\wangzhezhewang\\Documents\\'
output_dir = 'C:\\Users\\wangzhezhewang\\Documents\\'

# ********** ********** ********** **********
# define input files and global variables in this program
# ********** ********** ********** **********
input_file = 'percent-bachelors-degrees-women-usa.csv'
input_auto_file = 'auto-mpg.csv'
input_stocks_file = 'stocks.csv'

# ********** ********** ********** **********
# read input files
# ********** ********** ********** **********
perc_degree_women_df = pd.read_csv(input_dir + input_file)
print(perc_degree_women_df.columns)

auto = pd.read_csv(input_dir + input_auto_file)
print(auto.columns)

stocks_df = pd.read_csv(input_dir + input_stocks_file)
print(stocks_df.columns)

year = perc_degree_women_df['Year']
physical_sciences = perc_degree_women_df['Physical Sciences']
computer_science = perc_degree_women_df['Computer Science']
health = perc_degree_women_df['Health Professions']
education = perc_degree_women_df['Education']
print(type(year))

# ********** ********** ********** ********** ********** **********
# Chap1: Customizing plots
# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=2
# ********** **********
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, 'blue')
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, 'red')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=3
# ********** **********
# Create plot axes for the first line plot
plt.axes([0.05, 0.05, 0.425, 0.9])
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
# Create plot axes for the second line plot
plt.axes([0.525, 0.05, 0.425, 0.9])
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=4
# ********** **********
# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1,2,1)
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')
# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1,2,2)
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')
# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=5
# ********** **********
# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')
# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2,2,2)
# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')
# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)
# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')
# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)
# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')
# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=7
# ********** **********
# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red') 
plt.plot(year, physical_sciences, color='blue')
# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')
# Set the x-axis range
plt.xlim((1990, 2010))
# Set the y-axis range
plt.ylim((0, 50))
# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()
# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png')

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=8
# ********** **********
# Plot in blue the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='blue')
# Plot in red the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences,color='red')
# Set the x-axis and y-axis limits
plt.axis((1990, 2010, 0, 50))
# Show the figure
plt.show()
# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png')

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=10
# ********** **********
# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 
# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
# Add a legend at the lower center
plt.legend(loc='lower center')
# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=11
# ********** **********
# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()
# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]
# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')
# Add a black arrow annotation
plt.annotate('Maximum', xy = (yr_max, cs_max), xytext = (yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))
# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/customizing-plots?ex=12
# ********** **********
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Set the style to 'ggplot'
plt.style.use('ggplot')
# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 
# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')
# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')
# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))
# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')
# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')
# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()

# ********** ********** ********** ********** ********** **********
# Chap2: Plotting 2D arrays
# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=2
# ********** **********
# Import numpy and matplotlib.pyplot
# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)
# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u,v)
# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 
# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()
# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')

# ********** **********
Z = np.array([[1, 2, 3], [4, 5, 6]])
print('Z:\n', Z)
plt.pcolor(Z)
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=3
# ********** **********
A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])
plt.pcolor(A, cmap='Blues')
plt.colorbar()
plt.show()

# ********** **********
B =  np.array([[1, 2, 1], [0, 0, 1], [-1, 1, 1]])
plt.pcolor(B, cmap='Blues')
plt.colorbar()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=5
# ********** **********
print(Z)
# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)
# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X, Y, Z, 20)
# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(X,Y,Z)
# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(X,Y,Z, 20)
# Improve the spacing between subplots
plt.tight_layout()
# Display the figure
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=6
# ********** **********
print(Z)
# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')
# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')
# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')
# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')
# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=8
# ********** **********
# Generate a 2-D histogram
plt.hist2d(hp, mpg, range=((40,235), (8,48)) ,bins=(20,20) )
# Add a color bar to the histogram
plt.colorbar()
# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=9
# ********** **********
# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp, mpg, gridsize = (15, 12), extent=((40,235, 8,48)))
# Add a color bar to the histogram
plt.colorbar()
# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=11
# ********** **********
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')
# Print the shape of the image
print(img.shape)
# Display the image
plt.imshow(img)
# Hide the axes
plt.axis('off')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=12
# ********** **********
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')
# Print the shape of the image
print(type(img))
print(img.shape)
# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)
# Print the shape of the intensity
print(intensity.shape)
# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')
# Add a colorbar
plt.colorbar()
# Hide the axes and show the figure
plt.axis('off')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=13
# ********** **********
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')
# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2,2,1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5') 
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=0.5)
# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2,2,2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=1)
# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2,2,3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=2)
# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2,2,4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2,-1,0,1,2])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-2,2,-1,1), aspect=2)
# Improve spacing and display the figure
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/plotting-2d-arrays?ex=14
# ********** **********
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')
# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))
# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % (rescaled_image.min(), rescaled_image.max()))
# Display the rescaled image
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)
plt.show()

# ********** ********** ********** ********** ********** **********
# Chap3: Statistical plots with Seaborn
# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=2
# ********** **********
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x = 'weight', y='hp', data=auto)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=3
# ********** **********
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=4
# ********** **********
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')
# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='blue', label='First Order')
# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='green', order=2, label='Second Order')
# Add a legend and display the plot
plt.legend(loc = 'upper right')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=5
# ********** **********
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data = auto, hue = 'origin', palette = 'Set1')
plt.legend(loc = 'upper right')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=6
# ********** **********
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data = auto, row = 'origin', palette = 'Set1')
# Display the plot
plt.show()

# Plot linear regressions between 'weight' and 'hp' grouped column-wise by 'origin'
sns.lmplot(x='weight', y='hp', data = auto, col = 'origin', palette = 'Set1')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=8
# ********** ********** 
# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data = auto)
# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', data = auto, size = 3, jitter = True)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=9
# ********** **********
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'  
plt.subplot(2,1,1)
sns.swarmplot(x = 'cyl', y = 'hp', data = auto)
# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x = 'hp', y = 'cyl', data = auto, hue='origin', orient = 'h')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=10
# ********** **********
# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)
# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto, inner = None, color = 'lightgray')
# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto, jitter = True, size = 1.5)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=12
# ********** **********
# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x = 'hp', y = 'mpg', data = auto)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=13
# ********** **********
# Generate a joint plot of 'hp' and 'mpg' using a scatter plot
sns.jointplot(x = 'hp', y = 'mpg', data = auto, kind = 'scatter')
# Display the plot
plt.show()

# joint plot with regression plot
sns.jointplot(x = 'hp', y = 'mpg', data = auto, kind = 'reg')
plt.show()

# joint plot with residual plot
sns.jointplot(x = 'hp', y = 'mpg', data = auto, kind = 'resid')
plt.show()

# joint plot with kde, "kernel density estimate"
sns.jointplot(x = 'hp', y = 'mpg', data = auto, kind = 'kde')
plt.show()

# joint plot with hexin-point plot
sns.jointplot(x = 'hp', y = 'mpg', data = auto, kind = 'hex')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=14
# ********** **********
auto_02 = auto[['mpg', 'hp', 'origin']]
# Print the first 5 rows of the DataFrame
print(auto_02.head())
# Plot the pairwise joint distributions from the DataFrame
sns.pairplot(auto_02)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=15
# ********** **********
auto_02 = auto[['mpg', 'hp', 'origin']]
# Print the first 5 rows of the DataFrame
print(auto_02.head())
# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto_02, kind = 'reg', hue = 'origin')
# Display the plot
plt.show()

# ********** **********
auto_02 = auto[['mpg', 'hp', 'origin']]
# Print the first 5 rows of the DataFrame
print(auto_02.head())
# Plot the pairwise joint distributions grouped by 'origin' along with scatter
sns.pairplot(auto_02, kind = 'scatter', hue = 'origin')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/statistical-plots-with-seaborn?ex=16
# ********** **********
# Print the covariance matrix
cov_matrix = pd.DataFrame({'mpg': [1, -0.778, -0.832], 'hp': [-0.778, 1, 0.865], 'weight': [-0.832, 0.865, 1]})
cov_matrix.index = ['mpg', 'hp', 'weight']
print(cov_matrix)
# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)
# Display the heatmap
plt.show()

# ********** ********** ********** ********** ********** **********
# Chap4: Analyzing time series and images
# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=2
# ********** **********
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# stocks_02_df = stocks_df.copy()
# stocks_02_df['Date_YYYYMM'] = stocks_02_df['Date'].str[0:7]
aapl = stocks_df['AAPL']
ibm = stocks_df['IBM']
csco = stocks_df['CSCO']
msft = stocks_df['MSFT']
print(type(aapl))

# Plot the aapl time series in blue
plt.plot(aapl, color='blue', label='AAPL')
plt.show()
# Plot the ibm time series in green
plt.plot(ibm, color='green', label='IBM')
# Plot the csco time series in red
plt.plot(csco, color='red', label='CSCO')
# Plot the msft time series in magenta
plt.plot(msft, color='magenta', label='MSFT')
# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')
# Specify the orientation of the xticks
plt.xticks(rotation=60)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=3
# ********** **********
# Plot the series in the top subplot in blue
plt.subplot(2,1,1)
plt.xticks(rotation= 45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')
# Slice aapl from '2007' to '2008' inclusive: view
view = aapl['2007':'2008']
# Plot the sliced data in the bottom subplot in black
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=4
# ********** ********** 
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
stocks_02_df = stocks_df.copy()
stocks_02_df['Date_datetime'] = pd.to_datetime(stocks_02_df['Date'])
stocks_02_df.index = stocks_02_df['Date_datetime']

aapl = stocks_02_df['AAPL']
ibm = stocks_02_df['IBM']
csco = stocks_02_df['CSCO']
msft = stocks_02_df['MSFT']

# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view_1 = aapl['2007-11':'2008-04']
# Plot the sliced series in the top subplot in red
plt.subplot(2,1,1)
plt.plot(view_1, color = 'red')
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.xticks(rotation = 45)
plt.show()
# Reassign the series by slicing the month January 2008
view_2 = aapl['2008-01']
# Plot the sliced series in the bottom subplot in green
plt.subplot(2,1,2)
plt.plot(view_2, color = 'green')
plt.title('AAPL: Jan. 2008')
plt.xticks(rotation = 45)
# Improve spacing and display the plot
plt.tight_layout()
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=5
# ********** **********
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']
# Plot the entire series 
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')
# Specify the axes
plt.axes([0.25, 0.5, 0.35, 0.35])
# Plot the sliced series in red using the current axes
plt.plot(view, color = 'red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=8
# ********** **********
# Plot std_30 in red
plt.plot(std_30, color = 'red', label='30d')
# Plot std_75 in cyan
plt.plot(std_75, color = 'cyan', label='75d')
# Plot std_125 in green
plt.plot(std_125, color = 'green', label='125d')
# Plot std_250 in magenta
plt.plot(std_250, color = 'magenta', label='250d')
# Add a legend to the upper left
plt.legend(loc='upper left')
# Add a title
plt.title('Moving standard deviations')
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=11
# ********** **********
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')
# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap ='gray')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()
# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256), normed= True, color ='red', alpha = 0.4)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=12
# ********** **********
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')
# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()
# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')
# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0,256),
               normed=True, cumulative=True, 
               color='blue', alpha=0.4)
               
# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=13
# ********** **********
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()
# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)
# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)
# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')
# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False, color='red', alpha=0.4)
plt.grid('off')
# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')
# Add title
plt.title('PDF & CDF (equalized image)')
# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=14
# ********** **********
# Load the image into an array: image
image = plt.imread('hs-2004-32-b-small_web.jpg')
# Display image in top subplot
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image)
# Extract 2-D arrays of the RGB channels: red, green, blue
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
# Flatten the 2-D arrays of the RGB channels into 1-D
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()
# Overlay histograms of the pixels of each color in the bottom subplot
plt.subplot(2,1,2)
plt.title('Histograms from color image')
plt.xlim((0,256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)
# Display the plot
plt.show()

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/introduction-to-data-visualization-with-python/analyzing-time-series-and-images?ex=15
# ********** **********
# Load the image into an array: image
image = plt.imread('hs-2004-32-b-small_web.jpg')
# Extract RGB channels and flatten into 1-D array
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()
# Generate a 2-D histogram of the red and green pixels
plt.subplot(2,2,1)
plt.grid('off') 
plt.xticks(rotation=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels, green_pixels, bins=[32,32])
# Generate a 2-D histogram of the green and blue pixels
plt.subplot(2,2,2)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels, blue_pixels, bins=[32,32])
# Generate a 2-D histogram of the blue and red pixels
plt.subplot(2,2,3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.hist2d(blue_pixels, red_pixels, bins=[32,32])
# Display the plot
plt.show()

