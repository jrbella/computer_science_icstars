#Write your function here
def append_sum(lst):
  lst_sum = lst[-1] + lst[-2]
  lst.append(lst_sum)
  lst_sum = lst[-1] + lst[-2]
  lst.append(lst_sum)
  lst_sum = lst[-1] + lst[-2]
  lst.append(lst_sum)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))