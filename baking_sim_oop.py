class Entity:
    def __init__(self, name, money) -> None:
        self.name = name
        self.ingredients_inventory = {}
        self.cooked_inventory = {}
        self.money = money

    def buy_ingredient(self, item, quantity, price):
        pass

    def sell_ingredient(self, item, quantity, price):
        pass

    def cook_receipe(self, receipe):
        pass

    def buy_receipe(self, receipe, price):
        pass



player = Entity('Roven', 1000)
another_player = Entity('John', 2000)   
shop = Entity('Grocery', 1000000)

ended = False
while not ended:
    action = input("What would you like to do? ")
    if action == 'i':
        item = input("What would you like to buy? ")
        quantity = int(input("How many? "))
        price = int(input("How much? "))
        player.buy_ingredient(item, quantity, price)
        shop.sell_ingredient(item, quantity, price)
    elif action == 'c':
        receipe = input("What would you like to cook? ")
        player.cook_receipe(receipe)

