# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#     temp = lst[left]
#     lst[left] = lst[right]
#     lst[right] = temp
#     left = left + 1
#     right = right - 1
#   return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

# def reverse_list(lst):
#   # Create a new reversed list
#   reversed_lst = lst[::-1]
#   # Copy the elements back into the original list
#   for i in range(len(lst)):
#       lst[i] = reversed_lst[i]
#   return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#     temp = lst[left]
#     lst[left] = lst[right]
#     lst[right] = temp
#     left = left + 1
#     right = right - 1
#   return lst

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))

# def first_palindrome(words):
#   for word in words:
#     flag = 0
#     left = 0
#     right = len(word) - 1
#     while left < right:
#       if word[left] != word[right]:
#         flag = 1
#       left = left + 1
#       right = right - 1
#     if flag == 0:
#       return word

#   return ""


# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)


# omg it finally works!! could not tell you how i got there tho T-T
# def remove_duplicates(nums):
#   left = 0 
#   right = left + 1
#   while left < right and right < len(nums):
#     if nums[left] == nums[right]:
#       nums.pop(right)
#       right = left + 1 # this is pretty important tho. 
#       #wouldn't work without it 
#     else:
#       right += 1
#       left += 1
#   return nums

# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list
#-----Session 5-----
#problem 2
# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#     temp = lst[left]
#     lst[left] = lst[right]
#     lst[right] = temp
#     left = left + 1
#     right = right - 1
#   return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

# #problem 3
# def reverse_list(lst):
#   # Create a new reversed list
#   reversed_lst = lst[::-1]
#   # Copy the elements back into the original list
#   for i in range(len(lst)):
#       lst[i] = reversed_lst[i]
#   return lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(reverse_list(lst))

# #problem 4
# def reverse_list(lst):
#   left = 0
#   right = len(lst) - 1
#   while left < right:
#     temp = lst[left]
#     lst[left] = lst[right]
#     lst[right] = temp
#     left = left + 1
#     right = right - 1
#   return lst

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))

# #problem 5
# def first_palindrome(words):
#   for word in words:
#     flag = 0
#     left = 0
#     right = len(word) - 1
#     while left < right:
#       if word[left] != word[right]:
#         flag = 1
#       left = left + 1
#       right = right - 1
#     if flag == 0:
#       return word

#   return ""


# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)


# #omg it finally works!! could not tell you how i got there tho T-T

# #nicee

# #problem 6
# def remove_duplicates(nums):
#   left = 0 
#   right = left + 1
#   while left < right and right < len(nums):
#     if nums[left] == nums[right]:
#       nums.pop(right)
#       right = left + 1 # this is pretty important tho. 
#       #wouldn't work without it 
#     else:
#       right += 1
#       left += 1
#   return nums

# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list

#-----Session 6-----
#problem 1
#Problem 1 
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

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

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

g = [1,2,3]
s = [1,1,3]
print(find_content_children(g,s))
g = [1,1]
s = [2,2,2]
print(find_content_children(g,s))
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

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))