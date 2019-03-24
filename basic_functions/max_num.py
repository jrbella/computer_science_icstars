#Write your function here
def max_num(nums):
  largest_num = nums[0]
  for number in nums:
    if number > largest_num:
      largest_num = number
  return largest_num
  

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))