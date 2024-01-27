from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from wtforms import Form, SelectField, RadioField
from sklearn.preprocessing import OrdinalEncoder
import joblib  

app = Flask(__name__)

# Modeli yükle
model = joblib.load('final_model.sav')

# Form alanları buraya eklenecek
class TechnicalOptionForm(Form):
    Brand = SelectField('Brand', choices=[
        (0, 'Samsung'),
        (1, 'Xiaomi'),
        (2, 'Apple'),
        (3,'General Mobile'),
        (4, 'Oppo'),
        (5, 'Reeder'),   
        (6, 'Huawei'),
        (7, 'realme'),
        (8, 'Tecno'),
        (9, 'Infinix'),
        (10, 'POCO'),
        (11, 'Casper'),
        (12, 'Hiking'),
        (13, 'TCL'),
        (14, 'LG'),
        (15, 'Vivo'),
        (16, 'Alcatel')
    ])
    
    Internal_Storage = SelectField('Internal Storage', choices=[
        (6, "1 TB"),
        (5, "512 GB"),
        (3, "256 GB"),
        (0, "128 GB"),
        (1, "64 GB"),
        (2, "32 GB"),
        (4, "16 GB"),
        (7, "8 GB")
    ])

    RAM_Capacity = SelectField('RAM Capacity', choices=[
        (7, "32 GB"),
        (6, "12 GB"),
        (2, "8 GB"),
        (1, "6 GB"),
        (0, "4 GB"),
        (3, "3 GB"),
        (4, "2 GB"),
        (5, "1 GB")
    ])

    Display_Tech = SelectField('Display Technology', choices=[
        (2, "OLED"),
        (1, "AMOLED"),
        (0, "LCD")
    ])

    Screen_Res = SelectField('Screen Resolution', choices=[
        (2, "QHD"),
        (1, "HD"),
        (0, "FHD")
    ])

    Camera_Res = SelectField('Camera Resolution', choices=[
        (1, "Below 15 MP"),
        (0, "Above 15 MP")
    ])

    Battery_Capacity = SelectField('Battery Capacity', choices=[
        (6, "1000-2000 mAh"),
        (5, "2000-3000 mAh"),
        (3, "3500-4000 mAh"),
        (0, "4500-5000 mAh"),
        (1, "5000-6000 mAh"),
        (2, "4000-4500 mAh"),
        (4, "3000-3500 mAh"),
        (7, "800-1000 mAh"),
        (8, "6000-7000 mAh")
    ])

    Connection_Speed = SelectField('Connection Speed', choices=[
        (2, "4G"),
        (1, "5G"),
        (0, "4.5G"),
        (3, "3G"),
        (4, "2G"),
    ])
    
    Screen_Refresh_Rate = SelectField('Screen Refresh Rate',choices=[
        (5,"Above 144 Hz"),
        (4,"144 Hz"),
        (1,"120 Hz"),
        (2,"90 Hz"),
        (0,"60 Hz"),
        (3,"Below 60 Hz")
    ])

    Screen_Size = SelectField('Screen Size', choices=[
        (1, "Below 6 inch"),
        (0, "Above 6 inch"),
    ])
    
    
    Fingerprint_Scanner = RadioField("Fingerprint Scanner",choices=[
        (0,"Yes"),
        (1,"No")
    ],default = 0)
    
    Face_Recog   = RadioField("Face Recognition",choices=[
        (0,"Yes"),
        (1,"No")
    ],default = 0)
    
    Water_Dust_Resistance = RadioField("Water/Dust_Resistance",choices=[
        (1,"Yes"),
        (0,"No")
        
    ],default = 1,)
    
    Dual_SIM = RadioField("Dual SIM",choices=[
        (0,"Yes"),
        (1,"No")
    ],default = 0)
    
    Card_Slot = RadioField("Card Slot",choices=[
        (0,"Yes"),
        (1,"No")
    ],default = 0)
    
    OS = RadioField("OS", choices = [
        (0,'Android'),
        (1,'İOS')
    ],default = 0)

@app.route("/", methods=["GET", "POST"])
def index():
    form = TechnicalOptionForm(request.form)
    pred = "?"

    if request.method == "POST" and form.validate():
        # Formdan gelen veriyi al
        payload = {
            "Brand": float(request.form["Brand"]),
            "OS": float(request.form["OS"]),
            "Internal_Storage": float(request.form["Internal_Storage"]),
            "RAM_Capacity": float(request.form["RAM_Capacity"]),
            "Display_Tech": float(request.form["Display_Tech"]),
            "Screen_Res": float(request.form["Screen_Res"]),
            "Camera_Res": float(request.form["Camera_Res"]),
            "Battery_Capacity": float(request.form["Battery_Capacity"]),
            "Connection_Speed": float(request.form["Connection_Speed"]),
            "Screen_Size": float(request.form["Screen_Size"]),
            "Fingerprint_Scanner": float(request.form["Internal_Storage"]),
            "Face_Recog": float(request.form["Face_Recog"]),
            "Water_Dust_Resistance": float(request.form["Water_Dust_Resistance"]),
            "Dual_SIM": float(request.form["Dual_SIM"]),
            "Card_Slot": float(request.form["Card_Slot"]),
            "Screen_Refresh_Rate": float(request.form["Screen_Refresh_Rate"]),
        }
        
        
        # Modeli kullanarak tahmin yap
        pred_value = model.predict([list(payload.values())])[0]
        pred = f"{pred_value:.2f} TL"

    return render_template("result.html", form=form, pred=pred)

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=80, debug=True)