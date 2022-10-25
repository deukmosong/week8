try:
    10*(30/0)
except ZeroDivisionError:
    print('0으로 나눌려 했습니다')
try:
    x=int(input('정수 x를 입력하세요:'))
except ValueError:
    print('정수형이 아닙니다')
try:
    import sys
    f=open('myfile.txt')
    s=f.readLine()
except FileNotFoundError:
    print('파일을 찾을수가 없습니다')
