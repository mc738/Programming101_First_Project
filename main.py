import card
import data_structures

card.Card("", 2)

cd = data_structures.CardDeck([ 1, 2, 3, 4, 5 ])

print(cd.pick_random())
print(cd.count())
print(cd.take_random())
print(cd.count())


print("Hello, World!")