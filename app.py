from crypt import methods
from flask import Flask, url_for, redirect, render_template, request
import pickle
from wtforms import Form, validators, SelectField, RadioField
import requests

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def index():
    form = SelectField(request.form)
    pred = -99

    if request.method == "POST":
        payload = {
            "Brand": form.Brand.data,
            "Internal_Storage": form.Internal_Storage.data,
            "RAM_Capacity": form.RAM_Capacity.data,
            "Display_Tech": form.Display_Tech.data,
            "Screen_Res": form.Screen_Res.data,
            "Camera_Res": form.Camera_Res.data,
            "Battery_Capacity": form.Battery_Capacity.data,
            "Connection_Speed": form.Connection_Speed.data,
            "Screen_Size": form.Screen_Size.data,
            "Fingerprint_Scanner": form.Fingerprint_Scanner.data,
            "Face_Recog": form.Face_Recog.data,
            "Water_Dust_Resistance": form.Water_Dust_Resistance.data,
            "Dual_SIM": form.Dual_SIM.data,
            "Card_Slot": form.Card_Slot.data,
            "Screen_Refresh_Rate": form.Screen_Refresh_Rate.data,
        }