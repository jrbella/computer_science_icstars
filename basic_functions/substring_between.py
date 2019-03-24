<<<<<<< HEAD
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  if start not in word or end not in word:
    return word
  else:
    start_index = word.find(start) + 1
    slice1 = word[start_index:]
    end_index = slice1.find(end)
    end_index = (start_index + end_index)
    return word[start_index:end_index]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
=======
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  if start not in word or end not in word:
    return word
  else:
    start_index = word.find(start) + 1
    slice1 = word[start_index:]
    end_index = slice1.find(end)
    end_index = (start_index + end_index)
    return word[start_index:end_index]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
>>>>>>> 33165ef760f3f6cf715cc7e108bec10772e7e107
# should print "apple"