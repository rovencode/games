ingredients = ["eggs", "milk_bottle", "sugar", "cinnamon", "pumpkin", "apples", "flour", "butter", "vanilla extract", "cocoa"]
recipe_name = ["pumpkin_pie", "apple_pie", "cookies", "pudding"]

print("")
recipe = recipe_name[0] + ": " + ingredients[0] + ", " + ingredients[1] + ", " + ingredients[2] + ", " + ingredients[3] + ", " + ingredients[4] + ", " + ingredients[6] + ", " + ingredients[7]
print(recipe)
print("")

recipe = recipe_name[1] + ": " + ingredients[2] + ", " + ingredients[3] + ", " + ingredients[5] + ", " + ingredients[6] + ", " + ingredients[7]
print(recipe)
print("")

recipe = recipe_name[2] + ": " + ingredients[0] + ", " + ingredients[2] + ", " + ingredients[6] + ", " + ingredients[7] + ", " + ingredients[8]
print(recipe)
print("")

recipe = recipe_name[3] + ": " + ingredients[0] + ", " + ingredients[1] + ", " + ingredients[2] + ", " + ingredients[6] + ", " + ingredients[7] + ", " + ingredients[8] + ", " + ingredients[9]
print(recipe)
print("")

print("you can make stuff now")
print("to add or remove an ingredient, you just type: add {your ingredient} or subtract {your ingredient}")
print("lets get started")
print("")


player_input = str(input(""))
if player_input not in ingredients:
    



