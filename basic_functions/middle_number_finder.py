#Write your function here
def middle_element(lst):
  middle = int(len(lst)/2)
  if len(lst) % 2 == 0:
    second_middle = middle -1
    return (lst[middle] + lst[second_middle]) / 2
  else:
    return lst[middle]

#Uncomment the line below when your function is done
# should return (-10 + -4) /2 == -7.0
print(middle_element([5, 2, -10, -4, 4, 5]))
# should return -10
print(middle_element([5, 2, -10, -4, 4]))