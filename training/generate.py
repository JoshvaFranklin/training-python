# from random import choice
import random

number = random.randint(1, 10)
print(number)

if number %2 == 0:
    print("Even")
else:
    print("odd")
    
cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)
   
            

'''
coin = random.choice(["Heads","tails"])

print(coin)

#this is probability in action

'''