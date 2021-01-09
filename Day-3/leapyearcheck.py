year = int(input("Which year do you want to check? "))

check4 = year%4
check100 = year%100
check400 = year%400

if check4 == 0:
  if check100 == 0:
    if check400 == 0:
      print("leap year")
    else: print("not a leap year")
  else: print("leap year")
else: 
  print("Not Leap Year")


