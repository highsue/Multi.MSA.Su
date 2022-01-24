app = Flask(__name__)
@app.route("/") 
def FlaskLab(): 
    return "공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스" 

@app.route("/data1")
def FlaskData(): 
    keyValue =r"9XYEAg2P7uoRGqGJIn%2FPZ4KMMSirySVFYQ6CDZUisRAuaDnoHlTsf1PGv%2F74TxRhQtTZdY1F5dTghp0OgKDwWw%3D%3D"  
    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)  
    dataURL += "&cond" + "%5BorgZipaddr%3A%3ALIKE%5D"+"=종로구"
    dataURL += "&serviceKey=" + keyValue
    dataResult = requests.get(dataURL)
    return json.loads(dataResult)  D=%EC%A2%85%EB%A1%9C%EA%B5%AC"+"=종로구"
    dataURL += "&serviceKey=" + keyValue
    dataResult = requests.get(dataURL)
    return json.loads(dataResult)  
