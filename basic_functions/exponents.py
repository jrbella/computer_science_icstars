#Write your function here
def exponents(bases, powers):
  numbers = []
  for i in bases:
    for j in powers:
      numbers.append(i ** j)
  return numbers
    

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))