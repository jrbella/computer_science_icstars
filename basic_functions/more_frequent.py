#Write your function here
def more_frequent_item(lst, item1, item2):
  item_count1 = lst.count(item1)
  item_count2 = lst.count(item2)
  
  if item_count1 > item_count2:
    return item1
  elif item_count2 > item_count1:
    return item2
  else:
    return item1
  
#Uncomment the line below when your function is done
#Should return 3
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
#Should return 2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 2, 2, 2], 2, 3))
#Should return 2
print(more_frequent_item([2, 3, 2, 3, 2, 3, 2, 3], 2, 3))