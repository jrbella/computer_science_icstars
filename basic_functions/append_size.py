#Write your function here
def append_size(lst):
  num = len(lst)
  lst.append(num)
  return lst

#Uncomment the line below when your function is done
#should be [23, 42, 108, 3]
print(append_size([23, 42, 108]))
#should be [2, 1, 2]
print(append_size([2 ,1 ]))
