#Write your function here
def divisible_by_ten(nums):
  divisible = []
  for number in nums:
    if number % 10 == 0:
      divisible.append(number)
  return len(divisible)
		

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))