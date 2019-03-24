#Write your function here
def remove_middle(lst, start, end):
  new_lst = lst[:start] + lst[end:]
  new_lst.remove(lst[end])
  return new_lst
  

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
print(remove_middle([4, 8, 15, 16, 23], 2, 4))
#even number of numbers, the middle numbers are n/2 and (n/2)-1