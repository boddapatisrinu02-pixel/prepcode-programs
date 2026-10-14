a=int(input("enter number 1"))
b=int(input("enter number 2"))
operator=input("enter operator")
if operator=='+':
    print("add",a+b)
elif operator=='-':
    print("sub",a-b)
elif operator=='*':
    print("mul",a*b)
else:
    print("div",a/b)