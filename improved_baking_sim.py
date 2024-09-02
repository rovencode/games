import time
from random import randint

# Riha sucks :)

print("welcome to the baking simulator")
time.sleep(1)
print("you will be given a recipe and you will have to bake it")
time.sleep(1)
print("you will be given a list of ingredients and you will have to choose the correct amount of each ingredient")
time.sleep(1)
print("you will be given a list of tools and you will have to choose the correct tool for each step")
time.sleep(1)
print("you will be given a list of steps and you will have to choose the correct order of steps")
time.sleep(1)
print("you will be given a list of temperatures and you will have to choose the correct temperature for each step")
time.sleep(1)
print("you will be given a list of times and you will have to choose the correct time for each step")
time.sleep(1)
print("ok, lets get started")
print("")


recipe_names, tool, ingredient, temperature, time_ = ["cake", "cookies", "pie", "muffins", "bread", "brownies", "cupcakes", "pancakes", "waffles", "biscuits"], ["bowl", "spoon", "whisk", "knife", "pan", "oven", "measuring cup", "measuring spoon"], ["flour", "sugar", "butter", "eggs", "milk", "baking soda", "baking powder", "salt", "cinnamon", "vanilla extract"], ["350", "375", "400", "425", "450", "475", "500", "525", "550", "575"], ["10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]

def game_logic():

    global Win 
    global lose

    time.sleep(1)
    print(f"how many {ingredient_name} do you want to cook with?: ")
    answer_sum = randint(1, 3)
    answer_sum2 = (int(ingredient_num - answer_sum))
    answer_num = randint(1, 3)
    if answer_num == 3:

        choices = randint(1, 10) + randint(1, 10)
        print("1. " + str(choices))
        choices = randint(1, 10) + randint(1, 10)
        print("2. " + str(choices))
        choices = answer_sum2 + answer_sum
        print("3. " + str(choices))

    if answer_num == 2:
        
        choices = randint(1, 10) + randint(1, 10)
        print("1. " + str(choices))
        choices = answer_sum2 + answer_sum
        print("2. " + str(choices))
        choices = randint(1, 10) + randint(1, 10)
        print("3. " + str(choices))

    if answer_num == 1:
        
        choices = answer_sum2 + answer_sum
        print("1. " + str(choices))
        choices = randint(1, 10) + randint(1, 10)
        print("2. " + str(choices))
        choices = randint(1, 10) + randint(1, 10)
        print("3. " + str(choices))
    
    print("what is your answer?: ")
    answer = input("answer: ")
    if answer == answer_num:
        print("correct")
        print("lets do the next one")

    else:
        print("incorrect")
        print("you lose")
        lose = True

    print(f"what tool do you want to use for step {loop}?: ")
    answer_num = randint(1, 3)
    if answer_num == 3:

        choices = tool[randint(0, len(tool) - 1)]
        print("1. " + str(choices))
        choices = tool[randint(0, len(tool) - 1)]
        print("2. " + str(choices))
        choices = tool_name
        print("3. " + str(choices))

    if answer_num == 2:

        choices = tool[randint(0, len(tool) - 1)]
        print("1. " + str(choices))
        choices = tool_name
        print("2. " + str(choices))
        choices = tool[randint(0, len(tool) - 1)]
        print("3. " + str(choices))

    if answer_num == 1:

        choices = tool_name
        print("1. " + str(choices))
        choices = tool[randint(0, len(tool) - 1)]
        print("2. " + str(choices))
        choices = tool[randint(0, len(tool) - 1)]
        print("3. " + str(choices))

    print("what is your answer?: ")
    answer = input("answer: ")
    if answer == answer_num:
        print("correct")
        print("lets the next one")

    else:
        print("incorrect")
        print("you lose")
        lose = True

    print(f"what temperature do you want to heat step {loop} up to?: ")
    answer_num = randint(1, 3)
    answer_sum =  randint(1, 10)
    answer_sum2 = (int(temperature_num) - answer_sum)
    if answer_num == 3:

        choices = ((str(temperature[randint(0, len(temperature) - 1)]) - randint(1, 10)) + str(randint(1, 10)))
        print("1. " + str(choices))
        choices = ((str(temperature[randint(0, len(temperature) - 1)]) - randint(1, 10)) + str(randint(1, 10)))
        print("2. " + str(choices))
        choices = answer_sum2 + answer_sum
        print("3. " + str(choices))

    if answer_num == 2:

        choices = ((str(temperature[randint(0, len(temperature) - 1)]) - randint(1, 10)) + str(randint(1, 10)))
        print("1. " + str(choices))
        choices = answer_sum2 + answer_sum
        print("2. " + str(choices))
        choices = ((str(temperature[randint(0, len(temperature) - 1)]) - randint(1, 10)) + str(randint(1, 10)))
        print("3. " + str(choices))

    if answer_num == 1:

        choices = answer_sum2 + answer_sum
        print("1. " + str(choices))
        choices = temperature[randint(0, len(temperature) - 1)]
        print("2. " + str(choices))
        choices = temperature[randint(0, len(temperature) - 1)]
        print("3. " + str(choices))

    print("what is your answer?: ")
    answer = input("answer: ")
    if answer == answer_num:
        print("correct")
        print("lets do the last one")

    else:
        print("incorrect")
        print("you lose")
        lose = True

    print(f"how long does it take to cook step {loop}?: ")
    answer_num = randint(1, 3)
    answer_sum = randint(1, 10)
    answer_sum2 = (int(time_num) - answer_sum)

    if answer_num == 3:

        choices = time_[randint(0, len(time_) - 1)]
        print("1. " + str(choices))
        choices = time_[randint(0, len(time_) - 1)]
        print("2. " + str(choices))
        choices = answer_sum2 + time_num
        print("3. " + str(choices))

    if answer_num == 2:

        choices = time_[randint(0, len(time_) - 1)]
        print("1. " + str(choices))
        choices = answer_sum2 + time_num
        print("2. " + str(choices))
        choices = time_[randint(0, len(time_) - 1)]
        print("3. " + str(choices))

    if answer_num == 1:

        choices = answer_sum2 + time_num
        print("1. " + str(choices))
        choices = time_[randint(0, len(time_) - 1)]
        print("2. " + str(choices))
        choices = time_[randint(0, len(time_) - 1)]
        print("3. " + str(choices))

    print("what is your answer?: ")
    answer = input("answer: ")
    if answer == answer_num:
        print("correct")
        print("you win")
        Win = True

    

    else:
        print("incorrect")
        print("you lose")
        lose = True



lose = False
while lose == False or Win == True:

    recipe_name = recipe_names[randint(0, len(recipe_names) - 1)]
    print("")
    print(recipe_name + ":")
    step_num = randint(5, 12)

    for loop in range(1,step_num):

        recipe = [recipe_names[randint(0, len(recipe_names) - 1)], ingredient[randint(0, len(ingredient) - 1)], tool[randint(0, len(tool) - 1)], temperature[randint(0, len(temperature) - 1)], time_[randint(0, len(time_) - 1)]]

        recipe_name, ingredient_name, tool_name, temperature_num, time_num = recipe
        ingredient_num, tool_num = randint(4, 10), randint(1, 3)
        
        print("")
        print(str(loop) + ". " + str(ingredient_num) + " " + (ingredient_name), f"cook step {str(loop)} with " + str(tool_name), f"heat step {str(loop)} up to " + str(temperature_num), f"the time it takes to cook step {(loop)} is " + str(time_num))

    game_logic()