<<<<<<< HEAD
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  new_lst = []
  for data in word:
    if data in new_lst:
      continue
    else:
      new_lst.append(data)
  return len(new_lst)
    
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
=======
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  new_lst = []
  for data in word:
    if data in new_lst:
      continue
    else:
      new_lst.append(data)
  return len(new_lst)
    
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
>>>>>>> 33165ef760f3f6cf715cc7e108bec10772e7e107
# should print 4