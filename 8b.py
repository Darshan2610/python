from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Output to static HTML file
output_file("plot.html")

# Line plot
p1 = figure(title="Line Plot", x_axis_label="x", y_axis_label="y")
p1.line(x, y, legend_label="Line", line_width=2)

# Scatter plot
p2 = figure(title="Scatter Plot", x_axis_label="x", y_axis_label="y")
p2.scatter(x, y, legend_label="Points", size=8, color="navy")

# Bar plot
p3 = figure(title="Bar Plot", x_axis_label="x", y_axis_label="y")
p3.vbar(x=x, top=y, legend_label="Bars", width=0.5)

# Combine plots into a grid
plots = gridplot([[p1, p2], [p3]])

# Show the plots
show(plots)
