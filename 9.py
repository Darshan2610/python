import plotly.graph_objects as go

bill = [10, 20, 15, 30, 25, 14, 35, 60, 78, 54]
tip = [1, 2, 3, 4, 1, 2, 7, 3, 1, 6]
size = [2, 3, 4, 1, 3, 1, 4, 5, 6, 2]

fig = go.Figure()
scatter = go.Scatter3d(
    x=bill,
    y=tip,
    z=size,
    mode="markers",
    marker=dict(size=12, color=size, colorscale="rainbow", opacity=0.8),
)
fig.add_trace(scatter)

fig.update_layout(
    scene=dict(xaxis_title="Total Bill", yaxis_title="Tip", zaxis_title="Size")
)
fig.update_layout(title="3D Scatter Plot with Tips Dataset")

# Save the plot as an HTML file
fig.write_html("3d_scatter_plot_tips.html")
fig.show()
