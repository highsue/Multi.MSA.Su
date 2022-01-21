import json
#읽기
try:
    jsonFile = open("DataLab\\mydata.json", mode="r", encoding="utf-8")
    tempData = json.load(jsonFile)  
    resultDat1 = tempData["name"] 
    resultDat2 = tempData["age"] 
    resultDat3 = tempData["address"] 
    resultDat4 = tempData["email"]
    resultDat5 = tempData["empcheck"] 
    print("읽기성공")
    print(resultDat1, resultDat2, resultDat3, resultDat4, resultDat5)
except Exception as ex: 
    print("읽기실패")
else:
    jsonFile.close()
    print("jsonFile 종료")

jsonData1 = {
    "empid" : 12345678,
    "name" : "홍길동",
    "info" : [
        { "date1": "2022-01-21", "home": "서울시"},
        { "dep": "개발", "email": "aaa@aaa.co.kr"}
    ]
}

#쓰기 
try:
    writeFile = open("DataLab\\test.json", mode="w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
    print("쓰기성공")
except: 
    print("쓰기실패")
else:
    writeFile.close()
    print("writeFile 종료")
#디버깅 변수 선언함(임시)
temp = 0
