#-----Session 5-----
#problem 2
def reverse_list(lst):
  left = 0
  right = len(lst) - 1
  while left < right:
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp
    left = left + 1
    right = right - 1
  return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

#problem 3
def reverse_list(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for i in range(len(lst)):
      lst[i] = reversed_lst[i]
  return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

#problem 4
def reverse_list(lst):
  left = 0
  right = len(lst) - 1
  while left < right:
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp
    left = left + 1
    right = right - 1
  return lst

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))

#problem 5
def first_palindrome(words):
  for word in words:
    flag = 0
    left = 0
    right = len(word) - 1
    while left < right:
      if word[left] != word[right]:
        flag = 1
      left = left + 1
      right = right - 1
    if flag == 0:
      return word

  return ""

# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)

#omg it finally works!! could not tell you how i got there tho T-T

#nicee

#problem 6
def remove_duplicates(nums):
  left = 0 
  right = left + 1
  while left < right and right < len(nums):
    if nums[left] == nums[right]:
      nums.pop(right)
      right = left + 1 # this is pretty important tho. 
      #wouldn't work without it 
    else:
      right += 1
      left += 1
  return nums

# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list


#-----Session 6-----
#problem 1
def is_long_pressed(name, typed):
  var1 = 0  #name
  var2 = 0  #typed

  # nothing typed then return 
  if len(typed) == 0:
    return False

  #loop through both and if letters are the same then
  # increment both 
  while var2 < len(typed) and var1 < len(name):
    if name[var1] == typed[var2]:
      var1 += 1
      var2 += 1
    elif var2 > 0 and typed[var2] == typed[var2 - 1]:
      var2 += 1
    else:
      return False
  return True

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

#problem 2
def find_content_children(g,s):
  s.sort()
  g.sort()
  child = 0
  size = 0
  count = 0
  while size < len(s) and child < len(g):
    if(g[child]<=s[size]):
      child+=1
      size+=1
      count+=1
    else:
      size+=1
  return count

# g = [1,2,3]
# s = [1,1,3]
# print(find_content_children(g,s))
# g = [1,1]
# s = [2,2,2]
# print(find_content_children(g,s))
#should return 3

#Problem 3 
def valid_palindrome(s):
  left = 0
  right = len(s)-1
  count = 0
  flag = 0
  lis = list(s)
  while left < right:
    if lis[left] == lis[right]:
      left += 1
      right -= 1
      flag += 1
    elif lis[left] != lis[right] and count < 1:
      count += 1
      lis.pop(flag)
      left += 1
      right -= 1
      flag += 1
    else:
      return False
  return True

s = "aba"
s2 = "abca"
s3 = "abc"

# print(valid_palindrome(s))
# print(valid_palindrome(s2))
# print(valid_palindrome(s3))


#-----Session 7-----
#Problem 1
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types

# my_pokemon = Pokemon('Pikachu','Electric')
# print(my_pokemon)

#Problem 2-8
class Pokemon:
  def __init__(self, name, types, evolution=None):
      self.name = name
      self.types = types
      self.is_caught = False
      self.evolution = evolution

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught, # Output: "is_caught": False
      })

  def catch(self):
    self.is_caught = True

  def choose(self):
    if self.is_caught == True:
      print(f"{self.name} I choose you!")
    else:
      print(f"{self.name} is wild! Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
  lst = []
  for pokemon in my_pokemon:
    if pokemon_type in pokemon.types:
      lst.append(pokemon.name)
  return lst
  
def get_evolutionary_line(starter_pokemon):
  lst = []
  curr = starter_pokemon
  while(curr.evolution != None):
    lst.append(curr.name)
    curr = curr.evolution
  lst.append(curr.name)
  return lst

# initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)
#squirtle=Pokemon("Squirtle",["Water"])
# squirtle.print_pokemon()
# squirtle.is_caught = True
# squirtle.print_pokemon()

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)
# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)

#Problem 9 & 10
# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next

# node_one=Node('a')
# node_two=Node('b')

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next) 

# node_one.next=node_two

# print(node_one.value)
# print(node_one.next.value)
# print(node_two.value)

#Problem 11
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_4 = Node("Toad")
node_3 = Node("Toad",node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario",node_2)



node_1=Node("Mario")
node_2=Node("Luigi")
node_3=Node("Wario")
node_4=Node("Toad")

node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
#aproova I was thinking the same approach initially - Ryan
#:)
#I just saw the def above so the approch makes more sense to me now
#Thank you so much!!!
 #Very cool!
#Thanks guys! <3


#-----Session 8 ------
#Problem 1
#Problem 1
class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    opponent.hp -= self.damage
    if opponent.hp <= 0:
      opponent.hp = 0
      print(f'{opponent.name} fainted')
    else:
      print(f'{self.name} dealt {self.damage} damage to {opponent.name}')

# pikachu = Pokemon("Pikachu", 30, 20)
# bulbasaur = Pokemon("Bulbasaur", 20, 30) 

# opponent = bulbasaur
# pikachu.attack(opponent)

#Problem 2
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

lst = ["Jigglypuff", "Wigglytuff"]

# node_1 = Node(0)
# node_1.value = lst[0]
# node_2 = Node(0)
# node_2.value = lst[1]
# node_1.next = node_2

node_2 = Node(lst[1])
node_1 = Node(lst[0], node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

#Problem 3
def add_first(head, new_node):
  new_node.next = head
  return new_node

head = lst[0]
# print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
# print(node_1.value, "->", node_1.next.value)

#Problem 4
node_3 = Node(lst[2])
node_2 = Node(lst[1], node_3)
node_1 = Node(lst[0], node_2)

def get_tail(head):
  curr = head
  if head == None:
    return None
  while curr.next != None:
    curr = curr.next
  return curr.value

head = node_1
tail = get_tail(node_1)
#print(tail)

#Problem 5
def ll_replace(head, original, replacement):
  curr = head
  while curr != None:
    if curr.value == original:
      curr.value = replacement
    curr = curr.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")


# while head.next != None:
#   print(head.value)
#   head = head.next
# print(head.value)

#Problem 6
def listify_first_n(head, n):
  result = []
  curr = head
  count = 0

  while curr != None and count < n:
    result.append(curr.value)
    curr = curr.next
    count += 1

  return result

# linked list: a -> b -> c
head = 'a'
lst = listify_first_n(head,2)
# print(lst)

# linked list: j -> k -> l 
head2 = 'j'
lst2 = listify_first_n(head2,5)
# print(lst2)