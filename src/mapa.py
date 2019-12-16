import folium
from pymongo import MongoClient
from src import connectCollection as cc

def mapeo(precio, habs):
    db, col = cc.connectCollection('searchbestrent', 'api')
    query = list(col.find({"Rooms": habs, "Price":{"$lt":precio}}))
    mapa = folium.Map(location=[40.4167, -3.70325], zoom_start=12, tiles='Stamen Terrain')
    for house in query:
        folium.Marker(house['location']['coordinates'][::-1],
                     radius=2,
                     icon=folium.Icon(icon='home', color='darkblue'),
                     popup=house['Street'] + " "+ str(house['Price'])
                     ).add_to(mapa)
    mapa.save("./Output/mapas/mapa.html")