name=input('입력할 파일의 이름:')
f=open(name,'r')
name=name.replace(".txt","_upper.txt")
f2=open(name,'w')
s=f.readline().rstrip()
while s:
    print(s.upper())
    f2.write(s.upper(),'\n')
    f2.write('\n')
    s=f.readline().rstrip()
f.close()
f2.close()
###########2번문제
name=input('파일 이름을 입력하세요:')
f=open(name,'r')
s=f.readline().rstrip()
a=[]
while s:
    a.append(s)
    s=f.readline().rstrip()
for i in range(len(a)):
    print(a[-1-i])
    
