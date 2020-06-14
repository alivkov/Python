import folium

map = folium.Map([41.807036, 24.114701], zoom_start=13, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='Markers')

fg.add_child(folium.Marker(location = [41.807036, 24.114701], popup='Беглика', icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('map.html')
