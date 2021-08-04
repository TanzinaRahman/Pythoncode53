#Exception Handling part 2
try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter second Number : "))
    result = num1 / num2
    print(result)
except(ValueError,ZeroDivisionError):
    print("You have entered incorrect input.")


finally:
    print("Thanks!!!")
