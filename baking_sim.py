# Copyright Roven Shah

import time
EggNum = 0
SugarNum = 0
BakingSodaNum = 0
ToppingsNum = 0
Money = 346
list_of_bakes = []
def list_sell_sensing(ran, Mon_ct):
    for i in range(len(list_of_bakes)):
        x = -1
        x += 1
        if list_of_bakes[x] == ran:
            Money += Mon_ct
print("hello welcome to the baking sim")
time.sleep(1)
print("in this game you can buy, bake and sell")
time.sleep(1)
print("right now, you have nothing to bake with you should go to the shop")
time.sleep(1)
print("eggs are $12")
time.sleep(1)
print("sugar is $10")
time.sleep(1)
print("baking soda is $20")
time.sleep(1)
print("toppings are $14")
time.sleep(1)
print("you currently have $346")
time.sleep(1)
print("to buy something, you type: get {your item)")
time.sleep(1)
print("what would you like to buy")

continue_game = True
while continue_game:
    shop_selection = str(input(""))
    valid_values = [ "get egg", "get sugar", "get baking soda", "get toppings"]
    while shop_selection not in valid_values:
        if shop_selection == "get egg":
            EggNum += 1
            Money -= 12
            print(f"you have ${Money}")
            print(f"you have {EggNum} eggs")
        elif shop_selection == "get sugar":
            SugarNum += 1
            Money -= 12
            print(f"you have ${Money}")
            print(f"you have {SugarNum} sugar")
        elif shop_selection == "get baking soda":
            BakingSodaNum += 1
            Money -= 12
            print(f"you have ${Money}")
            print(f"you have {BakingSodaNum} Baking soda")
        elif shop_selection == "get toppings":
            ToppingsNum += 1
            Money -= 12
            print(f"you have ${Money}")
            print(f"you have {ToppingsNum} Baking soda")
        else:
            print("you can't type this")
            shop_selection = str(input(""))
    time.sleep(1)
    print("would you like to keep shopping")
    Shopping_loop_trigger = str(input(""))
    if Shopping_loop_trigger == "yes":
        print("type how many more rounds you want to shop")
        Shopping_loop_int = input("")
        valid_shopping_loop_values = ["a","b","c","d","e","f","g","h","i",]
        if Shopping_loop_int == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z": 
            while Shopping_loop_int != "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z":
                print("this is not an intger")
                time.sleep(1)
                print("try again")
                Shopping_loop_int = input("")
        for i in range(int(Shopping_loop_int)):
            shop_selection = str(input(""))
            while shop_selection != "get egg" or "get sugar" or "get baking soda" or "get toppings":
                if shop_selection == "get egg":
                    EggNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {EggNum} eggs")
                elif shop_selection == "get sugar":
                    SugarNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {SugarNum} sugar")
                elif shop_selection == "get baking soda":
                    BakingSodaNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {BakingSodaNum} Baking soda")
                elif shop_selection == "get toppings":
                    ToppingsNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {ToppingsNum} Baking soda")
                else:
                    print("you can't type this")
                    shop_selection = str(input(""))
    elif Shopping_loop_trigger == "no":
        if ToppingsNum < 2 and BakingSodaNum < 2 and SugarNum < 2 and EggNum < 2:
            print("you still have to shop")
            shop_selection = str(input(""))
            while shop_selection != "get egg" or "get sugar" or "get baking soda" or "get toppings":
                if shop_selection == "get egg":
                    EggNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {EggNum} eggs")
                elif shop_selection == "get sugar":
                    SugarNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {SugarNum} sugar")
                elif shop_selection == "get baking soda":
                    BakingSodaNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {BakingSodaNum} Baking soda")
                elif shop_selection == "get toppings":
                    ToppingsNum += 1
                    Money -= 12
                    print(f"you have ${Money}")
                    print(f"you have {ToppingsNum} Baking soda")
                else:
                    print("you can't type this")
                    shop_selection = str(input(""))
        else:
            print("ok, now you are ready to bake")
            time.sleep(1)
            print("here is what you can bake based on the amount of stuff you have")
            time.sleep(1)
            if ToppingsNum < 2 and BakingSodaNum < 2 and SugarNum < 2 and EggNum < 2:
                print("you can bake cookies")
                time.sleep(1)
                print("you can bake small dounuts")
                time.sleep(1)
                print("you can bake small muffins")
                time.sleep(1)
                print("to bake something, you will type, bake {your item}")
                time.sleep(1)
                print("you can bake now")
                Bake_item = str(input(""))
                while Bake_item != "bake cookie" or "bake small dounut" or "bake small muffin":
                    if Bake_item == "bake cookie":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("cookie")
                    elif Bake_item == "bake small dounut":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("small dounut")
                    elif Bake_item == "bake small muffin":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("small muffin")
                    else:
                        print("you can't type this")
                        Bake_item = str(input(""))
            elif ToppingsNum > 2 and BakingSodaNum > 2 and SugarNum > 2 and EggNum > 2:
                print("you can bake 5 cookies")
                time.sleep(1)
                print("you can bake large dounuts")
                time.sleep(1)
                print("you can bake crossonts")
                time.sleep(1)
                print("to bake something, you have to type, bake {your item}")
                time.sleep(1)
                print("you can bake now")
                Bake_item = str(input(""))
                while Bake_item != "bake 5 cookies" or "bake large dounut" or "bake large muffin":
                    if Bake_item == "bake 5 cookies":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("5 cookies")   
                    elif Bake_item == "bake large dounut":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("large dounut")
                    elif Bake_item == "bake large muffin":
                        ToppingsNum -= 1
                        BakingSodaNum -= 1
                        SugarNum -= 1
                        EggNum -= 1
                        list_of_bakes.append("large muffin")
                    else:
                        print("you can't type this")
                        Bake_item = str(input(""))
                        print("now, if you want, you can sell stuff for more money so you don't get bankruped")
                        time.sleep(1)
                        print("do you want to sell")
                        Sell_trigger = str(input(""))
                        while Sell_trigger != "no" or "yes":
                            if Sell_trigger == "no":
                                print("ok")
                                time.sleep(1)
                                print("lookes like you are ready to go to the shop")
                                time.sleep(1)
                                print("what would you like to buy")
                            elif Sell_trigger == "yes":
                                print("what would you like to sell")
                                Choose_sell = str(input(""))
                                if Choose_sell == "cookie":
                                    list_sell_sensing("cookie", 15)  
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                elif Choose_sell == "small dounut":
                                    list_sell_sensing("small dounut", 20)
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                elif Choose_sell == "small muffin":
                                    list_sell_sensing("small muffin", 20)
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                elif Choose_sell == "5 cookies":
                                    list_sell_sensing("5 cookies", 75)
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                elif Choose_sell == "large dounut":
                                    list_sell_sensing("large dounut", 60)
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                elif Choose_sell == "large muffin":
                                    list_sell_sensing("large muffin", 60)
                                    print("lookes like you are ready to go to the shop")
                                    time.sleep(1)
                                    print("what would you like to buy")
                                else:
                                    print("you can't type that")
                                    Sell_trigger = str(input(""))