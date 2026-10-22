# figure out if a number is odd or even
# use input() to get the number from the user
# show the user a warning if they dont  even a number
# maybe use "string" .isnumeric()
# tell the user if the number is even (2, 4) or odd (1, 5, 7)



number = input("please enter a number:")




def odd_or_even(number):
 if number.isnumeric():
    number = int(number)
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
 else:
    print("Invalid input. Please enter a valid number")





    
number = input("please enter a number:")
odd_or_even(number)
odd_or_even("12")