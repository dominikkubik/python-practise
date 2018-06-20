import folium
import pandas as pd

#import data from csv
data = pd.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")

fg1 = folium.FeatureGroup(name="Volcanoes map")
for lt, ln, el in zip(lat,lon, elev):
    fg1.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+" m", radius=6, fill_color=color_producer(el), color="grey", fill_opacity=0.7, fill=True))

map.add_child(fg1)

##My test map part
fg = folium.FeatureGroup(name="My test map")
fg.add_child(folium.Marker(location=[38.2,-99],popup="Test marker 1", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[38.8,-98],popup="Test marker 2", icon=folium.Icon(color="green")))
for coordinates in [[39.1, -99.1],[39.2, -99.3]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Test marker", icon=folium.Icon(color="blue")))
map.add_child(fg)

#how to add json file
fg0 = folium.FeatureGroup(name="JSON data map")
fg0.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg0)
map.add_child(folium.LayerControl())

map.save("Map1.html")
