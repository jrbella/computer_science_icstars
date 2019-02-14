#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum = sum + number
    if sum > 9000:
      break
  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))