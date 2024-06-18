def is_subsequence(lst, sequence):
  temp = []
  for i in lst:
    for j in sequence:
      if i == j:
        temp.append(i)
      else:
        break
  return temp
  # if temp == sequence:
  #   return True
  # else:
  #   return False
    
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))