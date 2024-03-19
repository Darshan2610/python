import plotly.express as px
data = {
'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Houston'],
'Lat': [29,32,35,39,40],
'Lon': [-74.0060, -122.4194, -118.2437, -87.6298, -95.3698],
'Population': [8175133, 870887, 3971883, 2716000, 2328000]
}
# Create a map
fig = px.scatter_geo(data, lat='Lat', lon='Lon', text='City', size='Population',
                    projection='natural earth', title='Population of Cities',color='City')
fig.update_traces(textposition='top center') 
fig.show()
