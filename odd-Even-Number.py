# get the number through the input command and convert the string to integer
# check if the number is odd or even

number_to_check = int(input("Please enter the number you want to check"))
is_odd_even = number_to_check % 2
if (is_odd_even == 0):
 print("The number is even")
else:
 print("The number is odd")
