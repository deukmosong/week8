f=open('hello.txt','a')
f.write('\nWelcome to Python')
print('hello.txt 파일:')
f=open('hello.txt','r')
s=f.readline()
while s:
    print(s,end='')
    s=f.readline()