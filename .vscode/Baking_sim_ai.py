# Shop data
shop_ingredients = {
    "eggs": 5.00,
    "milk": 8.45,
    "dough": 7.25,
    "flour": 8.65
}

shop_tools = {
    "mixer": 25,
    "oven": 50,
    "spatula": 10,
    "pan": 19
}

shop_recipes = {
    "cake": 100,
    "cookie": 50,
    "muffin": 130,
    "brownie": 90,
    "sugar waffers": 132
}

# Player data
budget = 125
inventory = []

def buy(item):
    global budget

    if item in shop_ingredients:
        price = shop_ingredients[item]
    elif item in shop_tools:
        price = shop_tools[item]
    elif item in shop_recipes:
        price = shop_recipes[item]
    else:
        print("That item is not in the shop.")
        return

    if budget < price:
        print("You don't have enough money to buy that.")
    else:
        budget -= price
        print(f"You bought {item} for ${price}")
        print(f"Your budget is now ${budget}")
        inventory.append(item)

def print_instructions():
    instructions = """
    Welcome to the baking sim.
    In this game you will buy ingredients, tools and recipes to cook with.
    Then you will cook products and sell them for money.

    Here are the tools, recipes, and ingredients that you can buy at the shop.

    ingredients:
    """
    for ingredient, price in shop_ingredients.items():
        instructions += f"{ingredient}: ${price}\n"

    instructions += "\ntools:\n"
    for tool, price in shop_tools.items():
        instructions += f"{tool}: ${price}\n"

    instructions += "\nrecipes:\n"
    for recipe, price in shop_recipes.items():
        instructions += f"{recipe}: ${price}\n"

    instructions += f"\nYou have ${budget} in budget.\n\nLet's get started.\n"
    print(instructions)

print_instructions()

# Prompt user to buy an item
buy_item = input("What would you like to buy? ")
buy(buy_item)




        

        