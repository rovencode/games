instructions = """

Welcome to the baking sim.
In this game you will buy ingredients, tools and recipes to cook with.
Then you will cook products and sell them for money.

Here are the tools, recipes, and ingredients that you can buy at the shop.

ingredients:

eggs: $5.00
milk: $8.45
dough: 7.25
flour:8.65

recipes:

cake: $100
cookie: $50
muffin: $130
brownie: $90
sugar waffers: $132

You have $125 in budget.
you also have an oven, a mixer, a spatula, a pan, a rack, and a bowl.

Lets get started.

"""

print(instructions)

shop_ingredients = ["eggs", "milk", "dough", "flour"]
shop_ingredient_prices = [5, 8.45, 7.25, 8.65]
shop_tools = ["oven","mixer","spatula","pan","rack","bowl"]
shop_recipes = ["cake", "cookie", "muffin", "brownie", "sugar waffer"]
shop_recipe_prices = [100,50,130,90,132]

recipes = [["eggs","eggs","flour","milk","dough","dough"],
           
           ["eggs","flour","milk","dough"],

           ["eggs","eggs","flour","flour","milk","dough"],

           ["eggs","flour","flour","milk"],

           ["eggs","flour","flour","milk","dough","dough"]]

# 0-cake, 1-cookie, 2-muffin, 3-brownie, 4-sugar waffers

inventory = []
food_inventory = []
budget = 1000
shop_tools = ["oven", "mixer", "spatula", "pan", "rack", "bowl"]

for i in range(len(shop_tools)):
    inventory.append(shop_tools[i])

def buy(item):
    global budget
    if item in shop_ingredients:

        index = shop_ingredients.index(item)
        price = shop_ingredient_prices[index]
        budget -= price
        if budget < 0:
            print("You don't have enough money to buy that.")
            budget += price

        else:
            
            print(f"You bought {item} for ${price}")
            print(f"Your budget is now ${budget}")
            inventory.append(item)

    elif item in shop_recipes:

        index = shop_recipes.index(item)
        price = shop_recipe_prices[index]
        budget -= price

        if budget < 0:
            print("You don't have enough money to buy that.")
            budget += price
        else:

            print(f"You bought the recipe for {item} for ${price}")
            print(f"Your budget is now ${budget}")
            inventory.append(item)
            if item == "cake":
                print("to cook a cake you need 2 eggs, 1 flour, 1 milk, 2 dough")
            elif item == "cookie":
                print("to cook a cookie you need 1 egg, 1 flour, 1 milk, 1 dough")
            elif item == "muffin":
                print("to cook a muffin you need 2 eggs, 2 flour, 1 milk, 2 dough")
            elif item == "brownie":
                print("to cook a brownie you need 1 egg, 2 flour, 1 milk")
            elif item == "sugar waffers":
                print("to cook sugar waffers you need 1 egg, 2 flour, 1 milk, 2 dough")

    else:
            print("That item is not in the shop.")

    return budget
            
            
    
def shop():
    global budget

    buy_item = input("What would you like to buy? ")
    buy(buy_item)
    shop_loop = input("would you like to buy anything else? ")

    if shop_loop == "yes":
        shop_loop_rounds = int(input("How many more items would you like to buy? "))
        print("ok")

        for i in range(shop_loop_rounds):
            buy_item = input("What would you like to buy? ")
            buy(buy_item)

def cook_item_():
    global budget
    
    print("ok now lets cook something\n")
    print("here are the things in your inventory\n")

    for i in range(len(inventory)):
        print(inventory[i])
        print("")

    cook_item = input("what would you like to cook? ")

    if cook_item in shop_recipes:

        if cook_item in inventory:

            index2 = shop_recipes.index(cook_item)

            for i in range(len(recipes[index2])):

                if recipes[index2][i] in inventory:
                    inventory.remove(recipes[index2][i])
                    dont_cook = False

                else:
                    print("You don't have the ingredients to cook that.")
                    dont_cook = True
                    break


            if dont_cook == False:
                print(f"You cooked {cook_item}")
                food_inventory.append(cook_item)
        else:
            print("You don't have the recipe to cook that.")
            cook_shop_loop = input("would you like to go shoping")
            if cook_shop_loop == "yes":
                shop()
            elif cook_shop_loop == "no":
                pass
    else:
        print("this dosent exist")

def cook():
    global budget

    cook_item_()
    cook_loop = input("would you like to cook anything else? ")

    if cook_loop == "yes":
        cook_loop_rounds = int(input("How many more items would you like to cook? "))
        print("ok")

        for i in range(cook_loop_rounds):
            cook_item_()
    else:
        pass
    print("ok now lets sell something now\n")

def sell_item_():
    global budget
    print("here is a list of the food that you cooked\n")
    for i in range(len(food_inventory)):
        fi = food_inventory[i]
        print(fi)
        if fi == "cake":
            print("price: $450")
            price = "450"
        elif fi == "cookie":
            print("price: $210")
            price = "210"
        elif fi == "muffin":
            print("price: $500")
            price = "500"
        elif fi == "brownie":
            print("price: $400")
            price = "400"
        elif fi == "sugar waffer":
            print("price: $480")
            price = "480"

        print("")
    sell_item = input("what would you like to sell? ")
    if sell_item in shop_recipes:
        if sell_item in food_inventory:
            food_inventory.remove(sell_item)
            print(f"You sold {sell_item} for ${price}")
            budget += int(price)
            print(f"you now have ${budget} in budget")

        else:
            print("You don't have that to sell.")
            
    else:
        print("this dosent exist")

def sell():
    global budget
    sell_item_()
    sell_loop = input("would you like to sell anything else? ")
    if sell_loop == "yes":
        sell_loop_rounds = int(input("How many more items would you like to sell? "))
        print("ok")

        for i in range(sell_loop_rounds):
            sell_item_()
    
def main():        
    global budget

    while True:
        shop()

        cook()

        sell()
        print("ok now lets shop again\n")

main()     