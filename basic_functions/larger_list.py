#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
#should return 5
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
#should return 10
print(larger_list([4, 10, 2], [-10, 2, 5, 10]))
#should return 5
print(larger_list([4, 10, 2, 5], [-10, 2, 5]))