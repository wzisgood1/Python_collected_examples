# -*- coding: utf-8 -*-
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

from bokeh.plotting import figure
from bokeh.io import output_file, show

# ********** ********** ********** **********
# define input and output directories, and current date
# ********** ********** ********** **********
input_dir  = 'C:\\Users\\wangzhezhewang\\Documents\\'
output_dir = 'C:\\Users\\wangzhezhewang\\Documents\\'

# ********** ********** ********** **********
# define input files and global variables in this program
# ********** ********** ********** **********
input_female_file = 'literacy_birth_rate.csv'
input_aapl_file = 'aapl.csv'
input_auto_file = 'auto-mpg.csv'

# ********** ********** ********** **********
# read input files
# ********** ********** ********** **********
input_female_df = pd.read_csv(input_dir + input_female_file)
print(input_female_df.columns)

input_aapl_df = pd.read_csv(input_dir + input_aapl_file)
print(input_aapl_df.columns)

input_auto_df = pd.read_csv(input_dir + input_auto_file)
print(input_auto_df.columns)

# ********** ********** ********** ********** ********** **********
# Chap1: Basic plotting with Bokeh
# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=3
# ********** **********
fertility = input_female_df['fertility'][0:162]
female_literacy = input_female_df['female literacy'][0:162]

print(len(fertility))
print(len(female_literacy))
# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label= 'female_literacy (% population)')
# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)
# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')
# Display the plot
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=4
# ********** **********
# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)
# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)
# Specify the name of the file
output_file('fert_lit_separate.html')
# Display the plot
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=5
# ********** **********
# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color = 'blue', size = 10, alpha = 0.8)
# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color = 'red', size = 10, alpha = 0.8)
# Specify the name of the file
output_file('fert_lit_separate_colors.html')
# Display the plot
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=7
# ********** **********
date = pd.to_datetime(input_aapl_df['date'])
price = input_aapl_df['close']
# Import figure from bokeh.plotting
from bokeh.plotting import figure
# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_type= 'datetime', x_axis_label='Date', y_axis_label='US Dollars')
# Plot date along the x axis and price along the y axis
print(date)
print(price)
p.line(date, price)
# Specify the name of the output file and show the result
output_file('line.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=8
from bokeh.plotting import figure
# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')
# Plot date along the x-axis and price along the y-axis
p.line(date, price)
# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color='white', size=4)
# Specify the name of the output file and show the result
output_file('line.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=9
# ********** **********
# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]
# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]
# Add patches to figure p with line_color=white for x and y
p.patches(x,y, line_color = 'white')
# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=11
# ********** **********
# Import numpy as np
import numpy as np
# Create array using np.linspace: x
x = np.linspace(0, 5, 100)
# Create array using np.cos: y
y = np.cos(x)
# Add circles at x and y
p = figure(x_axis_label='x_value', y_axis_label='y_value')
p.circle(x,y)
# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=12
# ********** **********
# Import pandas as pd
import pandas as pd
# Read in the CSV file: df
df = pd.read_csv(input_dir + 'auto-mpg.csv')
# Import figure from bokeh.plotting
from bokeh.plotting import figure
# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')
# Plot mpg vs hp by color
p.circle(df['hp'], df['mpg'], color= df['color'], size= 10)
# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=14
# ********** ********** 
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource
# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)
# Add circle glyphs to the figure p
p.circle(x='Year', y='Time', color = 'color', size = 8, source = source)
# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)

# ********** ********** ********** **********
# https://campus.datacamp.com/courses/interactive-data-visualization-with-bokeh/basic-plotting-with-bokeh?ex=16
