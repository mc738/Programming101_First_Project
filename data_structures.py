import random

class CardDeck:

    def __init__(self, items) -> None:
        self.all_items = items
        self.current_items = items

    def pick_random(self):
        return random.choice(self.current_items)

    def take_random(self):
        item = random.choice(self.current_items)
        self.current_items.remove(item)
        return item

    def take_next(self):
        return self.current_items.pop(1)
    
    def count(self):
        return len(self.current_items)
    
    def shuffle(self):
        random.shuffle(self.current_items)

    def debug(self):
        print(self.current_items)

    def reset_items(self):
        self.current_items = self.all_items
        

