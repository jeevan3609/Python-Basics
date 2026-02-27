user_input = int(input("Enter the number:"))
if user_input != 0:
    if user_input % 3 == 0 and user_input % 2 == 0 :
        print("fizzbuzz")
    elif user_input % 3 == 0 :
        print("Fizz")
    elif user_input % 2 == 0:
        print("buzz")

## another approach 

user_input = int(input("enter the number"))
if user_input % 3 == 0 and user_input % 2 == 0 and user_input!= 0:
    print("FizzBuzz")
elif user_input % 3 == 0 and user_input!= 0:
    print("Fizz")
elif user_input % 2 and user_input != 0:
    print("buzz")