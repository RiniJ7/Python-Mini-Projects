print("Welcome to the tip calculator!")

bill_amount = input("What is the total bill amount? ")
tip_amount = input("What is the tip percentage? ")
number_of_people = input("How many people are splitting the bill? ")

bill_amount_float = float(bill_amount)

tip_amount_value = bill_amount_float * (int(tip_amount)/100)
tip_amount_float = float(tip_amount_value)  

total_bill = bill_amount_float + tip_amount_float

cost_per_head = int(total_bill) / int(number_of_people)

print(f"Each person should pay $ {round(cost_per_head,2)}")
