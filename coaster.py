height = int(input("Enter Your Height:"))
credit = int(input("Enter Your Credit:"))
if height >= 137 and credit >= 10 :
  print("Enjoy the ride:")
elif height < 137 and credit >= 10 :
  print("You are not tall enhough to ride")
elif height >= 137 and credit < 10 :
  print("You do not have enough credits")
else :
  print("You have no met either the requirement")