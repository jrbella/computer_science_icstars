<<<<<<< HEAD
# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  word1_slice = word1[1:]
  word2_slice = word2[1:]
  phrase = "{0}{1} {2}{3}".format(word2[0], word1_slice, word1[0], word1_slice)

  return phrase
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
=======
# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  word1_slice = word1[1:]
  word2_slice = word2[1:]
  phrase = "{0}{1} {2}{3}".format(word2[0], word1_slice, word1[0], word1_slice)

  return phrase
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
>>>>>>> 33165ef760f3f6cf715cc7e108bec10772e7e107
# should print b a