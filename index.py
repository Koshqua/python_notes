#Importing packages
import http
import re

#Variables in python don't require any keyword to initialize; 
#You just put any name and assignment sign. 
my_var = "just a simple string"
print("Hello world " + my_var)
my_var.jo

another_var = "python \n supports \" escape characters"
print(another_var.upper())
string = "My string"
print(string.replace("My", "Your"))
string = string.replace("M", "P")
print(string)

#strings can be multiplied with * 
print(3 * 'ha') # hahaha

#two strings next to each other are automatically concatenated
s = 'This ' 'Is ' 'String' #This is string
print(s)    
s = ('Can be done '
    'In this way '
    'Just for readability')
print(s)

# if you don't want  special chars to be evaluated, you can put r in from of str declaration
# r stands for raw 
s = r'this\is\raw\string'

num = 5
#// absolute division returns int without floating point part
print(17 // 3)
# ** raises number to power 
print(3 ** 5)

# if we create expressions with mixed floating points and ints, ints will be converted to 
# floating points. 
print(3.5 + 4 * 2.1)

#str built-in function converts to string
string = str(num)
#abs returns the absolute number 
print(abs(-5)) #5
#pow returns the number powered by n 
print(pow(num, 2)) #25 
#min and max return max and min of collection of numbers
print("Max:" +str(max([2,1,3,5, 30])))
print("Min:" +str(min([12,3,3,5,5,4,1])))
#round rounds the floating numbers 
print("Round"+ str(round(3.2)))

#raw_input is the way to get user input from console
n = input("Enter your name :")
print("Hello, " + n + "!")


#================================================================================================
#lists(arrays) in python
#u can access item from zero, if u want to access from u can access it from -1
friends = ["Vasya", "Petya", "Vanya"]
print(friends[2] == friends[-1]) #Same elements

# u can use ranges of lists, it includes left side index and excludes right side index
print(friends[0:2])
# append adds one item to the list, extend adds another list to the end of list

#Lists are passed by reference(pointer)
friends_copy = friends
print(friends_copy)
friends.append("Peter")
print(friends_copy)
print(id(friends_copy))
print(id(friends))#Same address 


#================================================================================================
#it's possible to assign value to particular range of array 
ints = [1,2,3,4,5,6]
print("this are initial ints" + str(ints))
ints[1:5]= [5,4,3,2]
print(ints)
ints[1:3] = [] #deletes elements 


#================================================================================================
#Tuples are another data type in Python. Their unique point is that they are immutable. 
coordinates = (5,2,1)
#You can also access any value in tuple by square brackets, starting from 0 

#================================================================================================
#FUNCTIONS 
#The scope of function is defined by indentation, there are no curly brackets. 
#Only indented code will be counted as function body
#Word def is used to define a function. 
def sayhi(name):
    """ Function can start with string literal, which is docstring.
    Usually it's used to describe the function"""
    print("Hello, " + str(name))

sayhi(n)

#functions create their own scope. 
#and first, function will try to refer var in it's own scope, then enclosing func scope, and then global
#that means, that you cant assign new value to var outside of func
#and also, if you have two vars with the same name, func will first refer to local scope var
#so, unless you put global statement in front of gloabal var - u cant assign to them
#also, u cant assign to enclosing funcs vars, unless you put statement nonlocal in front of var
#
simple_string = "i am a string"
def another_func():
    simple_string = "assigning inside of func"
    print(simple_string)

another_func() #will show "assigning inside of func"

def sqrt(num):
    return num*num

print(sqrt(2))

#================================================================================================
#if statements are also written by ":" and indention.
if 2 < 4: 
    print("Two is less")
else:
    print("Will never happen")
#Instead of || and &&, python uses "or" and "and"
#else if in Python looks like elif
is_tall = True
is_male = True 
if is_tall and is_male:
    print("You are male and you are tall")
elif is_male and not(is_tall):
    print("You are male, but short")
else:
    print("You are neither male nor tall")
#instead of !condition in python we use not(condition)


#Dictionaries - are simply the maps in any other pl. 
myDictionary = {
    "key": "value",
    "any_key": [1,2,3],
}
#You can access dictionary value with square brackets 
print(myDictionary["key"])
#or you can access it with "get" function which allows you to specify default value, if key
#was not found 
print(myDictionary.get("other", "key is not valid"))

#================================================================================================

#while loops 
i = 0

while i <= 10:
    print(i)
    i += 1

#Guessing game 
secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count > 0:
        print("Try one more time")
    guess = input("Print your prediction: ")
    guess_count += 1
    if guess_count == guess_limit:
        out_of_guesses = True
    
if out_of_guesses:
    print("You went out of guesses")
else:
    print("You won!")


#For loops in Python work similar with for loops with ranges in go. 
friends = ["Johny", "Lizzy", "Bla-bla-bla"]

for friend in friends:
    print(friend)

#also it's possible to make ranges(indexes)
for index in range(10): #can be replaced with range(0,10)
    print(index) #prints ints from 0 to 9, the upper number is not included

for index in range(len(friends)):
    print()

#if to use else statement after for loops 
#it will executes in any case except the case when loop was terminated by break. 
for i in ints:
    if i % 2 == 0:
        print(str(i) + " is even")
        break
else:
    print("it will never get here")


def translate(expression):
    translation = ""
    for letter in expression:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation



print(translate(input("Enter a word to translate: ")))


#================================================================================================
#Classes are used to create our own types of data 
#To import Classes we use this construction
#from <module-name> import <class-name>
#__init__ function represents a function which creates and returns a new object.
# we simply specify the behaviour of how new obj will be initialised. 

class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    #we can also specify other functions(methods) for class
    def is_adult(self): #self should be specified as a first param
        if self.age >= 21:
            return True
        else:
            return False

#it calls the __init__ function from class 
person1 = Person("Ivan", 21, "Ukrainian")
print(person1.is_adult())


#Classes can inherit methods from other classes. 
#So they will be able to call them 
#For example, we can make class worker, which will inherit class person.

class Worker(Person): #in brackets we specify which class we want to inherit
    def do_some_work(self):
        print("Worker is doing something")
    #if we want to override method,which exists in inherited class, we just specify it one mre time
    #in class which inherits. Then it will refer to a newly specified method. 

w = Worker("Ivan", 33, "Ukrainian")
w.do_some_work()
w.is_adult() #we can call method, even though we didnt specify it. 


#================================================================================================
# range() function doesn't really return a list; 
# it returns a data structure, that behaves like list when you iterate over it. 
# if we wan't to make a list out of range() result we can use 
print(list(range(10))) #actual list
print(range(10)) #range(0,10)
#it doesn't return a list to save memory 


#statement pass is just placeholder, when syntactically programm needs statement
#but logically it needs to do nothing 
class emptyClass:
    pass
#or when you are working on new code 
def initlog():
    pass #implement it later 
#or like this 
if True:
    pass

#python supports one line variables assingment
a,b,c = 1,2,3
#expressions on right side  are evaluated before assignment happens.
#they evaluate starting from left to right 
a,b = b+1,a+1
print(a, b)