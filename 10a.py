import plotly.express as px
import pandas as pd


data = pd.read_csv("rain.csv")
# date = ['1/2/23', '4/5/23','7/7/23', '9/8/23','12/10/23'] # D,
# temp = [9, 6 ,8,2,10] # °C

fig = px.line(
    data,
    x="date",
    y="temp",
    title="Time Series Plot",
    labels={"date": "temp"},
    line_shape="linear",
    markers="D",
)
fig.update_traces(line=dict(color="yellowgreen"))

fig.show()
