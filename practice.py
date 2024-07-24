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

#Day 3
#Problem 1 & 2
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# Recreate this list in a single line of code
head = Node("Ash")
misty = Node("Misty")
brock = Node("Brock")
head.next.next = Node()

head =  Node('Ash',Node('Misty', Node('Brock')))

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def frequency_map(head):
  curr = head
  occ = {}
  while curr:
    if curr.value in occ:
      occ[curr.value] += 1
    else:
      occ[curr.value] = 1
    curr = curr.next
  return occ

# head = Node(1, Node(2, Node(3, Node(4, Node(2, Node(3))))))
# result = frequency_map(head)
# print(result)
\
#Problem 1
def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])

# print(insert_stars('abc'))

def insert_starss(s):
  temp = ''
  for i in range(len(s)-1):
    temp += s[i] + '*'
  temp += s[-1]
  return temp

# print(insert_starss('abc'))

#Problem 2
def string_length(s):
  if len(s) == 0:
    return 0
  else:
    return 1 + string_length(s[1:])

print(string_length('abc'))

#Problem 3