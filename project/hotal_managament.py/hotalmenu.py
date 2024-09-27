#define the menu of resturent

menu={
    'pizza':40,
    'burger':30,
    'fries':10,
    'soda':10,
    'salad':50
}


#Greet
print("welcome to resturent")
for key, value in menu.items():
    print(f"{key} = {value}")

order_total = 0   
item1=(input("place your food = "))

if item1 in menu:
    order_total=order_total+menu[item1]
    print(f'your oder placed{item1}')

else:
    print("its not in our menu ")    


another_order=input("do you want any other order (yes/no)")
if another_order=="yes":
    item2=input("next item =")
    if item2 in menu:
        order_total=order_total+menu[item2]
        print(f'you order is palced {item2}')
    else:
        print(f"its not in our menu[")


print(f'the total amout is {order_total}')        
