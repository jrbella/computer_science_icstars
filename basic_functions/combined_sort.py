#Write your function here
def combine_sort(lst1, lst2):
  new_lst = lst1 + lst2
  new_lst.sort()
  return new_lst

#Uncomment the line below when your function is done
#should return [-10, 2, 2, 4, 5, 5, 10, 10]
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
#shoudl return [-1, 1]
print(combine_sort([1], [-1]))