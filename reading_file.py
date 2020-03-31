#In python files are opened by open() func
#There are different options for opening files.
#r - read only, w - write, a - append(you can only add new data, but can't change)
#r+ - read and write 
file = open("file.txt", "r+")
#Checks if file is readable
print("File is readable: " + str(file.readable()))
#Reads the whole file and returns array of str
print(file.readlines())

#Read first line and moves "cursor" to next line
print(file.readline()) #first line
print(file.readline()) #second line 

#Will start reading from the "cursor" point left by two previous methods
for employee in file.readlines():
    print(employee)


# need to close files once we opened them 
file.close()