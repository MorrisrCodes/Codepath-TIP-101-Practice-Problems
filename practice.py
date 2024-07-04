#4th of july practice
#Problem 1-3
class Card():

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def is_valid(self):
    suits = ['Hearts','Spades','Clubs','Diamonds']
    ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    if self.suit in suits and self.rank in ranks:
      return True
    return False


def print_card(self):
  print(f"{self.rank} of {self.suit}")


# card = Card('Clubs', 'Ace')
# print_card(card)

# card = Card('Hearts', 'Clubs')
# print_card(card)

my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())
