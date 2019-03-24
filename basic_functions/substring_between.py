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
# should print "apple"