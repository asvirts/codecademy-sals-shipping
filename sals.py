weight = 31

# Ground Shipping

if weight <= 2:
  print("$1.50 + $20 flat charge = $21.50"
elif weight > 2 or weight <= 6:
  print("$3.00 + $20 flat charge = $23.00")
elif weight > 6 or weight <= 10:
  print("$4.00 + $20 flat charge = $24.00")
else:
  print("$4.75 + $20 flat charge = $24.75")