sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for item in location:
    scoops_sold += item
    
print(scoops_sold)
    
def scoops_sold(lst,scoops_sold):
  scoops_sold = scoops_sold
  for item in lst:
    for scoop in item:
      scoops_sold += scoop
print(scoops_sold)
 
scoops_sold(sales_data, 0)