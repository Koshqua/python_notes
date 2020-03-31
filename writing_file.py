# to write to the file you need to open it with "w" or "a" mode.
# if you open in w-mode and write - it will override a file
# if you open in a-mode and write - it will add content to the end of existing file

file = open("file.txt", "a")
file.write("Nathan Ten Napel\n")
#will append to the end

file.close()

file = open("file.txt", "r")
employees = file.readlines()
file.close()

file = open("file.txt", "w")
print(employees)
employees = employees[:len(employees)-1]
print(employees)
string = ""
string = string.join(employees)
print(string)
file.write(string)

