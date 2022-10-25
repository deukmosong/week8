f=open("number1to10.txt",'r')
f1=open("numberby10.txt",'w')
f2=open("merge.txt",'w')
a=f.readline().rstrip()
while a:
    a=int(a)
    b=a*10
    b=str(b)
    f1.write(b)
    f1.write('\n')
    f2.write('{}:{}'.format(a,b))
    f2.write('\n')
    a=f.readline().rstrip()