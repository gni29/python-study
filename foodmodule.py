'''
from modules.mylib import food
print(food.name)
food.cook()
food.eat()
from modules.mylib.food import cook, name, eat
print(name)
cook()
eat()
'''
from bbb.cm2 import add

print(add(3,4))