instructions = """

Welcome to the baking sim.
In this game you will buy ingredients, tools and recipes to cook with.
Then you will cok products and sell them for money.

Here are the tools, recipes, and ingredients that you can buy at the shop.

ingredients:

eggs: $5.00
milk: $8.45
dough: 7.25
flour:8.65

tools:

mixer: $25
oven: $50
spatula: $10
pan: $19

recipes:

cake: $100
cookie: $50
muffin: $130
brownie: $90
sugar waffers: $132

You have $125 in buget.

Lets get started.

"""

print(instructions)

shop_ingredients = ["eggs", "milk", "dough", "flour"]
shop_ingredient_prices = [5, 8.45, 7.25, 8.65]
shop_tools = ["mixer","oven", "spatula", "pan"]
shop_tool_prices = [25,50,10,19]
shop_recipes = ["cake", "cookie", "muffin", "brownie", "sugar waffers"]
shop_recipe_prices = [100,50,130,90,132]

def get_price(item):
    if item in shop_ingredients:
        index = shop_ingredients.index(item)
        price = shop_ingredient_prices[index]
        return price
    elif item in shop_tools:
        index = shop_tools.index(item)
        price = shop_tool_prices[index]
        return price
    elif item in shop_recipes:
        index = shop_recipes.index(item)
        price = shop_recipe_prices[index]
        return price
    else:
        return None

def buy(item, budget, inventory):
    price = get_price(item)
    if price is None:
        print("That item is not in the shop.")
    elif price > budget:
        print("You don't have enough money to buy that.")
    else:
        print(f"You bought {item} for ${price}")
        budget -= price
        print(f"Your budget is now ${budget}")
        inventory.append(item)
    return budget

def main():
    budget = 125
    inventory = []

    while budget > 0:
        item = input("What would you like to buy? ")
        budget = buy(item, budget, inventory)

# run the program
main() 