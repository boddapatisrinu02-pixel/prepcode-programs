amount=int(input("enter the amount"))
mem_ship=input("have membership yes/no")
if amount>=1000 or mem_ship=='yes':
    print("free delivery")
else:
    print("no free delivery")