'''
The speciality is the GeoJson library. The example shows putting of marker along the borders on a openstreet map.
'''

import folium, os

import pandas as pd

data = pd.read_csv('vol.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['VOL'])

m1= folium.Map(location=[23,90])
fg = folium.FeatureGroup(name='TawMap')

for i,j,k in zip(lat,lon, names):
    fg.add_child( folium.Marker(location=[i,j], popup=k, icon=folium.Icon(color='green'))     )

m1.add_child(fg)

'''
loc1=[23,90]; loc2=[23.1,90.1]
m = folium.Map(location = loc1)
folium.Marker(loc1, popup='im pop', icon=folium.Icon(color='red')   ).add_to(m)
folium.Circle(radius=1000, location=loc2, color='red', fill=False, name='L1').add_to(m)
folium.CircleMarker(radius=10, location=loc2, color='green', fill=True, name='L2').add_to(m)
#m.add_child(folium.LatLngPopup())

folium.LayerControl().add_to(m)
'''



m1.save('fol.html')
print('ok', m1 )


print(data)
