def every_three_nums(start):
  lst = list(range(start, 101, 3))
  if start <= 100:
    return lst
  else:
    return []
  

#Uncomment the line below when your function is done
print(every_three_nums(91))
print(every_three_nums(100))
print(every_three_nums(101))