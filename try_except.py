
#Try Except is used to catch errors and do some actions instead of just crashing the program.
#We can specify what kind of errors we want to check and what according actions we want to take.
try:
    number = int(input("Input a number: "))
    impossible = number/0
except ValueError as err:
    print(err)
except ZeroDivisionError as err: #it's possible to use variables for errors, to display their text
    print(err)