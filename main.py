from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd 

df = pd.read_csv('cars.csv')

#Create ColumnDataSource from data
source = ColumnDataSource(df)

#Create car list
car_list = source.data['Car'].tolist()

output_file('index.html')

#Add Plot
p = figure(
    title = 'Car with Highest Horsepower',
    y_range = car_list,
    plot_width = 800,
    plot_height = 600,
    x_axis_label = 'Horsepower',
    #y_axis_label = 'Y Axis',
    tools = 'pan, box_select, zoom_in, zoom_out, save, reset'
)

#Render glyph
p.hbar(
    y = 'Car',
    right = 'Horsepower',
    left = 0,
    height = 0.4,
    color = 'orange',
    fill_alpha = 0.5,
    source = source
)

#Add tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
    	<h3>@Car</h3>
    	<div><strong>Price: @Price</strong></div>
    	<div><strong>HP: @Horsepower</strong></div>
    	<div><img src="@Image" width=200px></div>
    </div>
"""

p.add_tools(hover)

#Show
save(p)