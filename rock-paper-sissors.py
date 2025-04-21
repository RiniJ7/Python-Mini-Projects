import random

rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print ("Welcome to Rock Paper Sissors Game!!")
print (f'print 1 for rock {rock}')
print (f'print 2 for paper {paper}')
print (f'print 3 for scissors {scissors}')

userChoice = int(input("please enter your choice : "))
if userChoice == 1:
    print (f'User choice : {rock}')
elif userChoice == 2:
    print (f'User choice : {paper}')
elif userChoice == 3:
    print (f'User choice : {scissors}')

computerChoice = int(random.randint(1,3))
if computerChoice == 1:
    print (f'Computer choice : {rock}')
elif computerChoice == 2:
    print (f'Computer choice : {paper}')
elif computerChoice == 3:
    print (f'Computer choice : {scissors}')

if userChoice == computerChoice:
    print (" This game is a tie")
elif userChoice == 1 and computerChoice == 2:
    print(f'the winner is computer')
elif userChoice == 2 and computerChoice == 1:
    print(f'the winner is user')
elif userChoice ==  2 and computerChoice == 3:
    print(f'the winner is computer')
elif userChoice == 3 and computerChoice == 2:
    print(f'the winner is user')
elif userChoice == 3 and computerChoice == 1:
    print(f'the winner is computer')
elif userChoice == 1 and computerChoice == 3:
    print(f'the winner is user')