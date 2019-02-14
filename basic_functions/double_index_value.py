#Write your function here
def double_index(lst, index):
  if len(lst) > int(index):
    value = lst[index]
    value = value *2
    lst[index] = value
    return lst
  else:
    print("index " + str(index) + " is outside the range of the list")
    

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
print(double_index([-3, -8, 10 , -12], 5))