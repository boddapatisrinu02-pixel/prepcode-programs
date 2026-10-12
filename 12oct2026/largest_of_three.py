a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
if b<a and c<a:
    print("a is largest")
elif a<b and c<b:
    print("b is largest")
else:
    print("c is largest")
