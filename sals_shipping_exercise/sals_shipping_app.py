ground_flat_charge = 20.0
drone_flat_charge = 0.0

def cost_of_ground_shipping(weight):
  if weight <= 2:
    return weight * 1.5 + ground_flat_charge
  elif weight <= 6 and weight > 2:
    return weight * 3.0 + ground_flat_charge
  elif weight <= 10 and weight > 6:
    return weight * 4.0 + ground_flat_charge
  else:
    return weight * 4.75 + ground_flat_charge
  
#unit test  
price = cost_of_ground_shipping(8.4)
print(price)

def cost_of_drone_shipping(weight):
  if weight <= 2:
    return weight * 4.5 + drone_flat_charge
  elif weight <= 6 and weight > 2:
    return weight * 9.0 + drone_flat_charge
  elif weight <= 10 and weight > 6:
    return weight * 12.0 + drone_flat_charge
  else:
    return weight * 14.25 + drone_flat_charge

#unit test
price_with_drone = cost_of_drone_shipping(1.5)
print(price_with_drone)

def best_shipping_price(weight):
  ground = cost_of_ground_shipping(weight)
  drone = cost_of_drone_shipping(weight)
  
  if ground < drone:
    print("The ground shipping is cheaper, it will cost $" + str(ground))
    return ground
  elif drone < ground:
    print("The drone shipping is cheaper, it will cost $" + str(drone))
    return drone

    
#unit test
best_price = best_shipping_price(12) #should be 77
#return value of best price
#print(best_price)
  