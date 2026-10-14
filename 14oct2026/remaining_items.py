product=int(input("enter no.of product"))
boxes=int(input("enter no.of boxes"))
filled_boxes=product//boxes
remain_product=product%boxes
print("filled boxes",filled_boxes)
print("remain product",remain_product)