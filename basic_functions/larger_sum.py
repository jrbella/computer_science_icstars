#Write your function here
def larger_sum(lst1, lst2):
  my_value1 = 0
  my_value2 = 0
  for number in lst1:
    my_value1 = my_value1 + number
  for number in lst2:
    my_value2 = my_value2 + number
  if my_value1 > my_value2:
    return lst1
  elif my_value2 > my_value1:
    return lst2
  else:
    return lst1