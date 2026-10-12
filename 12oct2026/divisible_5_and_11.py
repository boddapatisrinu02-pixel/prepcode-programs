num=int(input("enter num"))
if (num%5==0 and num%11==0):
    print("divisible by both")
elif(num%5==0):
    print("dvisible by 5 only")
elif(num%11==0):
    print("divisible by 11 only")
else:
    print("not divisible by both")