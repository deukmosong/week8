p=open("radin30.txt",'r')
s=p.readline()
lista=[0,0,0,0,0,0,0,0,0,0,0,0]
num_list=list(map(int, s.split(' ')))
print(num_list)
for i in range(0,len(num_list)):
  lista[num_list[i]]=lista[num_list[i]]+1
for i in range(1,11):
    print('{} :{}개'.format(i,lista[i]))