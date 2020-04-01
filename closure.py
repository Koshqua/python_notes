def enclosing(num):
    num *= 2
    def inner():
        another_num = num * 2
        return another_num
    return inner

func = enclosing(2)
print(func)
print(func())


#closure can be easily made with lambda expressions 
#lambda expression is just a small anonymous function

def outer(num):
    return lambda x, y: x * num + y
#so x and y are the arguments which closure function will accept
#and function body is specified after " : "
closure = outer(42)
print(closure(2,3))
print(closure(3, 20))

