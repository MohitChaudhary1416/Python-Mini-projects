menu = {
    "Momo": 100,
    "Chaumin" : 80,
    "Chiya" : 25,
    "Coffee": 50,
    "Pizza" : 350
}

print("Welcome To Mohit Resturent")
print("Momo: Rs100\nChaumin: Rs80\nChiya: Rs25\nCoffee: Rs50\nPizza: Rs350")
order_total = 0

item_1 = input("Enter the item you want to order = ").title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} is added to your order")
else:
    print(f"{item_1} is not available")

another_order = input("Do you want to order another item (Yes/No): ").title()
if another_order == "Yes":
    item_2 = input("Enter order you want to = ").title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} is added to your order")
    else:
        print(f"{item_2} is not availbale")

another_order1 = input("Do you Want to order another item (Yes/No)").title()
if another_order1 == "Yes":
    item_3 = input("Enter order you want to = ").title()
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"{item_3} is added to your order")
    else:
        print(f"{item_3} is not available")

print(f"The total sum of your is = {order_total}")
print("Thank you for choosing us please visit again")

