
price= int(input("enter price "))
print(type(price))
bad_history = True
if bad_history:
    print("you have bad history, you have only 10 poerncent discount")
    discount= price*10/100
    price = price-discount
    print("your price will be",price)
#test