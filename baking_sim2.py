user = {
            "name":"Bugs Bunny", 
            "money":100, 
            "bought_items":{}
       }

available_items = {'eggs':100, 'baking soda':50, "toppings":200, "sugar":50}
item_cost = {'eggs':1, 'baking soda':2, "toppings":3, "sugar":4}

def buy_item(user, quantity):
    user_items = user["bought_items"]

    if item in available_items:
        if available_items[item] >= quantity:

            if user["money"] >= item_cost[item]*quantity:
                user["money"] -= item_cost[item]*quantity
                available_items[item] -= quantity
                if item in user_items:
                    user_items[item] += quantity
                else:
                    user_items[item] = quantity

                print("You bought {} {}.".format(quantity, item))
            else:
                print("Sorry, you don't have enough money to buy {} {}.".format(quantity, item))
        else:
            print("Sorry, we don't have enough {}.".format(item))
    else:
        print("Sorry, we don't sell {}.".format(item))

input(f"Hello {user['name']}! Welcome to the baking simulator! Press enter to continue.")

print("Here is a list of items you can buy:")
for item in available_items:
    print(item)

print(f"You have {user['money']} to spend.")

while True:
    item = input("What would you like to buy? ")
    if item == "done":
        break
    if not item.isdigit():
        print("Please enter a valid item.")
        continue
    quantity = int(input("How many would you like to buy? "))
    buy_item(user, quantity)

print("You have bought:")

for item, quantity in user["bought_items"].items():
    print("{} {}".format(item, quantity))

print("Thank you for playing!")
