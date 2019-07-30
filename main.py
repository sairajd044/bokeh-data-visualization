from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import OrRd8
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
    fill_alpha = 0.9,
    fill_color = factor_cmap(
        'Car',
        palette = OrRd8,
        factors = car_list
    ),
    legend = 'Car',
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

#Add legend based on Car
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

#Show
save(p)
