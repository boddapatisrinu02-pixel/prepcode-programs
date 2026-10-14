datas=input()
data=datas.split()
salary=int(data[0])
hir=int(data[1])*salary/100
da=int(data[2])*salary/100
pf=int(data[3])*salary/100
allo=data[4]
if allo == 'a':
    print(salary+hir+da-pf+1500)
elif allo == 'b':
    print(salary+hir+da-pf+1700)
else:
    print(salary+hir+da-pf+2000)