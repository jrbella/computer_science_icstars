# Write your x_length_words function here:
def x_length_words(word, x):
  lines = word.split()
  for line in lines:
    if len(line) < x:
      return False
    else:
      return True
  
# Uncomment these function calls to test your  function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True