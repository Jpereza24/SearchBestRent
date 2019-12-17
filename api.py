from flask import Flask, request
from src import connectCollection as cc
from bson.json_util import dumps
import json
import folium
app=Flask(__name__)

@app.route("/hello")
def hello():
    return "Hola caracola!"

@app.route("/", methods=['GET'])
def complete():
    #Get the complete database from Mongo Atlas
    return dumps(coll.find())


@app.route("/<price>/<rooms>", methods=['GET'])
def query(price,rooms):
    #The function returns the houses that have the requirements of price and rooms that the user wants.
    pedido=list(coll.find({"Rooms":int(rooms), "Price":{"$lte":int(price)}}))
    mapa = folium.Map(location=[40.4167, -3.70325], zoom_start=12, tiles='Stamen Terrain')
    for house in pedido:
        folium.Marker(house['location']['coordinates'][::-1],
                     radius=2,
                     icon=folium.Icon(icon='home', color='darkblue'),
                     popup=house['Street'] + " "+ str(house['Price'])
                     ).add_to(mapa)
    return mapa._repr_html_()

@app.route("/list/<district>/", methods=['GET'])
def listdistrict(district):
    #It should return all the houses from a district.
    return dumps(coll.find({"District":str(district)}, {"Street":1, "Price":1, "_id":0}))


db,coll = cc.connectCollection("Pisos", 'total')

if __name__=="__main__":
    app.run(debug=True)
