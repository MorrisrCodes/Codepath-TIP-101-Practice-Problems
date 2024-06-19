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

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
