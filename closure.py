def enclosing(num):
    num *= 2
    def inner():
        another_num = num * 2
        return another_num
    return inner

func = enclosing(2)
print(func)
print(func())
