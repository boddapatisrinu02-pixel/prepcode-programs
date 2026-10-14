price=int(input("enter price"))
discount=int(input("enter discount"))
discount_amount=(discount*price)/100
print("discount_amount",discount_amount)
print("total amount",price-discount_amount)