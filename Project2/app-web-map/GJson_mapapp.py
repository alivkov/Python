import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    elif elevation > 3000:
        return 'red'

html = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s ft
"""

map = folium.Map([41.694410, -114.361793], zoom_start=5, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Markers')

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), fill=True, color='grey', fill_color = color_producer(el), fill_opacity=1.0))

map.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), name='Polygons', style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('map_html_GeoJson_colour.html')
