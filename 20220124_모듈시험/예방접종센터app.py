from flask import Flask
import json
import requests

app = Flask(__name__)
@app.route("/") 
def FlaskLab(): 
    return "공공데이터활용지원센터_코로나19 예방접종센터 조회서비스" 

@app.route("/data1")
def FlaskData(): 
    keyValue = r"9XYEAg2P7uoRGqGJIn%2FPZ4KMMSirySVFYQ6CDZUisRAuaDnoHlTsf1PGv%2F74TxRhQtTZdY1F5dTghp0OgKDwWw%3D%3D"
    dataURL = "https://api.odcloud.kr/api/15077586/v1/centers?"
    dataURL += "page="+ str(1) + "&perPage=" + str(10)  
    dataURL += "&serviceKey=" + keyValue
    dataResult = requests.get(dataURL)
    return json.loasd(dataResult)  
