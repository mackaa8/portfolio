#IMPORT keyword
import random

coin = random.choice(["heads", "tails"])
print(coin)

#keyword FROM (more specific importing)
from random import choice

coin = choice(["heads", "tails"])
print(coin)

#Another random function - randitn(a,b) - chooses a random integer between a and b 
import random

number = random.randint(1, 10)
print(number)

#random.shuffle(x) - puts values in a random order
import random

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

#STATISTICS library
import statistics

print(statistics.mean([100, 90]))


