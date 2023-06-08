import random
# from random import choice

coinToss = random.choice(["heads", "tails"])
print(coinToss)

print("********************************")

randomNumber = random.randint(1, 10)
print(randomNumber)

print("********************************")

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
    print(card)