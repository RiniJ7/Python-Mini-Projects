#using complex loops to code a ticketing system. make sure to use a flowchart before coding


height = int(input("Please enter your height?"))
if(height > 120):
    print("You are eligible for this ride")
    print("Adult tickets are $12 per head")
    print("Youth tickets are $7 per head")
    print("Kids tickets are $5 per head")
    category = input("Please enter the ticket category(Adult/Youth/Kids)")
    if(category == "Adult"):
        bill = 12
        print(" Your bill is $12")
    elif(category == "Youth"):
        bill = 7
        print(" Your bill is $7")
    elif(category == "Kids"):
        bill = 5
        print(" Your bill is $5")
    wants_photo = input ("Do you want to have a photo taken? Type y for yes and n for No")
    if wants_photo == 'y':
        bill += 3
    print (f"Your bill is ${bill}")
else:
    print("Sorry, you do not meet the requirements for this ride")    
                   