#4th of july practice
#Problem 1-5
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

  def get_value(self):
    ranks10 = ['2','3','4','5','6','7','8','9','10']
    higher = {'Jack':11,'Queen':12,'King':13}
    if self.rank in ranks10:
      return self.rank
    else:
        return higher.get(self.rank)
def print_card(self):
  print(f"{self.rank} of {self.suit}")

#card = Card('Clubs', 'Ace')
#print_card(card)

#card = Card('Hearts', 'Clubs')
#print_card(card)

#my_card = Card("Hearts", "7")
#print(my_card.is_valid())

#second_draw = Card("Spades", "Joker")
#print(second_draw.is_valid())

#card = Card("Hearts", "7")
#print(card.get_value())

#card_two = Card("Spades", "Jack")
#print(card_two.get_value())

#Problem 6
class Hand:
  def __init__(self):
      self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]

#day2practice
#Problem 1
def sum13(nums):
  pointer1 = 0
  count = 0
  while pointer1 < len(nums):
    if nums[pointer1] == 13:
      pointer1 += 2
    else:
      count += nums[pointer1]
      pointer1 += 1
  return count

#Problem 2
def sum67(nums):
  pointer = 0
  truth = False
  count = 0
  while pointer < len(nums):
    if nums[pointer] == 6:
      truth = True
    if truth == True:
      if nums[pointer] == 7:
        truth = False
      pointer += 1
    else:
      count += nums[pointer]
      pointer += 1
  return count