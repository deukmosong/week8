f=open('hello.txt','r')
s=f.readline()
print('hello.txt 파일:')
while s:
    print(s,end='')
    s=f.readline()