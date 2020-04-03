#functions can have default values. 
#it makes possible to call function with fewer arguments
def power(number, power=2, message="The power was "):
    return message + str(power)+" and result is " + str(number ** power)
#we can call func with only one arg 
print(power(10))


#to note, if you want to use vars from outer scope for arg's default values. 
#default values are evaluated in definition scope, so, if we defined, and used variable inside
#the value of default value will not change 
i = 5 
def print_int(num = i):
    print(num)

i = 6 
print_int() #will print five

#default values are evaluated only once for function definition. 
#so we can affect them with every call and change it. 
#it can come in handy, when there is mutable structure inside, like obj or list

def append_and_return(elem, L = []):
    L.append(elem)
    return L

#can be used similarly to iota in go
print(append_and_return(1)) #[1]
print(append_and_return(2)) #[1,2]
print(append_and_return(3)) #[1,2,3]

#if you dont want to be attached to the order of args in func when u call it,
#u can used key=value notation in call 

print(append_and_return(elem=4))


#func can accept arbitraty amount of args and interpret them as tuple 
# * makes a tuple out of sequence of args 
def arbitraty(*args):
    for arg in args:
        print(arg)

arbitraty(1,23,45,6,6,7,7,2)

#we can make opposite by * operator
#if we have list or tuple, we can create sequence of seperate args 

print(list(range(*[1,10]))) #*[1,10] returns 1,10 

def desribed():
    '''First line describes function briefly
    
    Second line should be blank. Rest describe func in details.
    '''
    pass

# it's possible to restrict using keyword only or position only arguments in function call
# by default, u can use both, position and keyword 
# by putting "/" in the end of list of args, you will restrict to pass only args by position on call
# "/" is used to separate pos only arguments from rest of them 
def key_only (*,arg, arg2=None):
    pass

key_only("string", 2)

#it comes in python 3.8 
# def pos_only(arg1, /, arg2):
#     pass


#we can annotate function (it's arguments and output result)
#it has no influence on the way code is written.
#it's used only for documenting 

def my_func(one: str, two: str) -> str:
    return one + two

print(my_func("ti ", "loh"))




