total_bill = input("what was the total bill? $")
percentage_tip = input("how much percentage you would like to tip? ")
total_people = input("how many people you want to split the bill? ")

bill_float = float(total_bill)
tip_int = int(percentage_tip)
people_int = int(total_people)

total_tip = (bill_float*tip_int)/100
total_amount = bill_float + total_tip

bill_split = total_amount/people_int
final_amount = round(bill_split, 2)
finalbill = str(final_amount)

print(f"everyone should pay ${finalbill} each")