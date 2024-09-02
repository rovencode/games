import random
from random import randint
import time

def g_intro():
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
    print("")

def g_recipe(ingredient_name, ingredient_num, tool_name, tool_num, temperature_num, time_num):
      
    print((ingredient_num) + " of " + (ingredient_name) + ", " + (tool_num) +  " of " + (tool_name) + ", " + "the temperature is " + (temperature_num) + ", " + "the time to bake this is " + (time_num))

g_intro()

class Recipe:

    def generate_recipe():

        global recipe_namex
        recipe_list = ["cake", "cookies", "pie", "muffins", "bread", "brownies", "cupcakes", "pancakes", "waffles", "biscuits"]
        recipe_namex = random.choice(recipe_list)
        return recipe_namex

    def generate_ingredients():

        global ingredient_namex
        global ingredient_numx
        ingredient_list = ["flour", "sugar", "butter", "eggs", "milk", "baking soda", "baking powder", "salt", "cinnamon", "vanilla extract"]
        ingredient_namex = random.choice(ingredient_list)
        ingredient_numx = random.randint(1, 10)
        return ingredient_namex, ingredient_numx


    def generate_tools():
        
        global tool_namex
        global tool_numx
        tool_list = ["bowl", "spoon", "whisk", "knife", "pan", "oven", "measuring cup", "measuring spoon"]
        tool_namex = random.choice(tool_list)
        tool_numx = (1)
        return tool_namex, tool_numx

    def generate_temperature():
        
        global temperature_numx
        temperature_list = ["350", "400", "450", "300", "325", "375", "425", "475", "500", "550"]
        temperature_numx = random.choice(temperature_list)
        return temperature_numx


    def generate_time():
        
        global time_numx
        time_list = ["10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
        time_numx = random.choice(time_list)
        return time_numx

lose = False

while lose == False:

    step_numx = randint(6, 13)

    time.sleep(1)
    Recipe.generate_recipe()
    print(str("               " + recipe_namex))
    print("")

    for loop in range(step_numx):

        Recipe.generate_ingredients()
        Recipe.generate_tools()
        Recipe.generate_temperature()
        Recipe.generate_time()

        g_recipe(str(ingredient_namex), str(ingredient_numx), str(tool_namex), str(tool_numx), str(temperature_numx), str(time_numx))
        lose = True
