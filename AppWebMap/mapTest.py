import folium
import pandas
# map=folium.Map(location=[38.58,-99.09], zoom_start=6,tiles="OpenStreetMap")
map=folium.Map(location=[8.8483542,76.9128092], zoom_start=6)
tile = folium.TileLayer('Mapbox Bright').add_to(map)
tile = folium.TileLayer('Mapbox Control Room').add_to(map)
tile = folium.TileLayer('Stamen Terrain').add_to(map)
tile = folium.TileLayer('Stamen Toner').add_to(map)
tile = folium.TileLayer('stamenwatercolor').add_to(map)
tile = folium.TileLayer('cartodbpositron').add_to(map)
tile = folium.TileLayer('cartodbdark_matter').add_to(map)
# map.add_child(folium.Marker(location=[8.853724, 76.924407], popup='Hi I am here', icon=folium.Icon(color='green')))
# 8.8546419,76.9239883

# print(dir(folium.map))
# print(help(folium.map))
df=pandas.read_csv('coor.txt')
lat=list(df['lat'])
lon=list(df['long'])
info=list(df['info'])
ele=list(df['ele'])

def color_producer(el):
	if el<50:
		return 'green'
	elif 50<= el <120:
		return 'orange'
	else:
		return 'red'

fg=folium.FeatureGroup(name="My marker")

for lt,ln,msg,el in zip(lat,lon,info,ele):
	fg.add_child(folium.Marker(location=[lt,ln], popup=msg, icon=folium.Icon(color=color_producer(el))))

# for coordinate in coordinates:
# 	fg.add_child(folium.Marker(location=list(str(coordinate).rstrip()), popup='Hi I am here', icon=folium.Icon(color='green')))
# 	# print(str(coordinate).rstrip())
fg1=folium.FeatureGroup(name="Population marker")
fg1.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
	style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
	else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fg)
map.add_child(fg1)

map.add_child(folium.LayerControl())
map.save('map2.html')
  