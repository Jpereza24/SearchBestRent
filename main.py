from flask import Flask, request, render_template
from src import connectCollection as cc
from bson.json_util import dumps
import json
import re
import folium
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hola caracola!"

@app.route("/price/rooms", methods=['POST'])
def map_price_rooms():
    #The function returns the houses that have the requirements of price and rooms that the user wants.
    price= request.form.get("price")
    rooms= request.form.get("rooms")
    pedido=list(coll.find({"Rooms":int(rooms), "Price":{"$lte":int(price)}}))
    mapa = folium.Map(location=[40.4167, -3.70325], zoom_start=12, tiles='Stamen Terrain')
    for house in pedido:
        folium.Marker(house['location']['coordinates'][::-1],
                     radius=2,
                     icon=folium.Icon(icon='home', color='darkblue'),
                     popup="Street: " + house['Street'] + " "+ "Price: " + str(house['Price']) + " €"
                     ).add_to(mapa)
    return mapa._repr_html_()

@app.route("/district/propertyt/m2/rooms", methods=['POST'])
def prediction():
    #This function returns the prediction of the value you can get from renting a house.
    query = list(coll.find())
    district=request.form.get("district")
    propertyt=request.form.get("propertyt")
    m2=request.form.get("m2")
    rooms=request.form.get("rooms")
    df = pd.DataFrame(query)
    df.Property_Type = df.Property_Type.replace({'flat':1, 'penthouse':2, 'studio':3, 'duplex':4, 'chalet':5, 'countryHouse':6})
    df.District=df.District.replace({'salamanca':1, 'centro':2, 'chamartin':3, 'chamberi':4, 'tetuan':5, 'moncloa':6, 'retiro':7, 'hortaleza':8, 'arganzuela':9, '':10})
    columns = ['Street', 'location']
    df.drop(columns, axis=1, inplace=True)
    X = df[['District', 'Property_Type', 'm2', 'Rooms']]
    y = df['Price']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)
    reg = GradientBoostingRegressor()
    reg.fit(X_train, y_train)
    prueba = pd.DataFrame({"District":int(district), "Property_Type":int(propertyt), "m2":int(m2), "Rooms":int(rooms)}, index=[0])
    d= reg.predict(prueba)
    pred = float(d)
    pred = round(pred, 2)
    pred = str(pred)
    pred = re.sub("\[","", pred)
    pred = re.sub("\]","", pred)
    return render_template("pred.html", pred=pred)

@app.route("/list/<district>/", methods=['GET'])
def listdistrict(district):
    #It should return all the houses from a district.
    return dumps(coll.find({"District":str(district)}, {"Street":1, "Price":1, "_id":0}))

db,coll = cc.connectCollection("Pisos", 'total')

if __name__=="__main__":
    app.run(debug=True)
