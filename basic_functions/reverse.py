# Write your reverse_string function here:
def reverse_string(word):
  lst = ""
  for i in range(len(word)-1,-1,-1):
    print(word[i])
    lst += (word[i])
  return lst
  
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print