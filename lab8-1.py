a=[10,20,30]
print(a[3])
##########2
n=int('20%')
##############3
a=100+'200'

try:
    a=[10,20,30]
    print(a[3])
except Exception as e:
    print('error :', e)
try:
    n=int('20%')
except Exception as e:
    print('error :', e)
try:
   a=100+'200'
except Exception as e:
    print('error :', e)
    