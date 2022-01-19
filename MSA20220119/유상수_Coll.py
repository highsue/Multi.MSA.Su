#1 Dictionary를 이용해서 평균 점수 구하기
#:{'국어':95, '영어':90, '수학':85, '과학':50}
point = {'국어':95, '영어':90, '수학':85, '과학':50}
dicData1 = point['국어']
dicData2 = point['영어']
dicData3 = point['수학']
dicData4 = point['과학']
average = (dicData1 + dicData2 + dicData3 + dicData4) / 4

#2. set을 이용해서 1~100까지 숫자 중에 공배수를 구함: 
# 3과 5의 공배수를 구하고, 합집합 구하기 & 표현식이용. 반복문의 리스트 형식 i for i range(100)
setData = set(range(1,101))  # 1~ 100까지
setData2 = set([i for i in range(1,101) if i % 3 == 0 ]) #3의 배수와 5의 공배수
setData3 = set([i for i in range(1,101) if i % 5 == 0]) #5의 배수
resultSetData = setData2 & setData3 #3의 배수와 5의 공배수 
resultSetData2 = setData2 | setData3 # 3의 배수와 5의 배수의 합집합

# 리스트 데이터 : 7,5,3,1,-1,-3-,5,-7 출력: range이용
listData = list(range(7,-8,-2))
resultData = listData[4]
print(listData)

#4. 4번째의 결과를 튜플로 변경(형변환)
changeData = list(resultData)
tupleData = tuple(changeData)  

# 'int' object is not iterable 문제가 해결이안됬습니다. 죄송합니다. 

# 디버깅을 위한 임시 변수
temp = 0
