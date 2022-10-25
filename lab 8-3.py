a=[1,2,3,4,5]
b=['첫번째','두번쨰','세번째','네번째','다섯번째']
findpostion=int(input('a의 요소를 선택하십시오:'))
for i in range(len(a)):
    if findpostion==a[i]:
        print("{}는 {} 요소입니다".format(i+1,b[i]))
########################222222222번
a=[1,2,3,4,5]
b=['첫번째','두번쨰','세번째','네번째','다섯번째']
try:
    findpostion=int(input('a의 요소를 선택하십시오:'))
    for i in range(len(a)):
        if findpostion==a[i]:
            print("{}는 {} 요소입니다".format(i+1,b[i]))
except ValueError:
    print('오류 :입력값이 정수나 실수가 아님')

