#using complex loops to code a ticketing system. make sure to use a flowchart before coding


height = int(input("Please enter your height?"))
if(height >= 120):
    print("You are eligible for this ride")
    print("Adult tickets are $12 per head")
    print("Youth tickets are $7 per head")
    print("Kids tickets are $5 per head")
    age = int(input("What is your age?"))
    if age < 12 :
        bill = 5
        print(f" Your bill is ${bill}")
    elif age < 18:
        bill = 7
        print(f" Your bill is ${bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be okay and have a free ride on us!")
    else:
        bill = 12
        print(f" Your bill is ${bill}")
    wants_photo = input ("Do you want to have a photo taken? Type y for yes and n for No")
    if wants_photo == 'y':
        bill += 3
        print(f" Your bill is ${bill}")
else:
    print("Sorry, you do not meet the requirements for this ride")    
                   