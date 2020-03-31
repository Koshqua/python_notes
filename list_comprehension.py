#list comprehension is an elegant way to create lists from other lists
#it has three parts
# 1 - is output expression 
# 2 - is input sequence 
# 3 - is variable, representing member of sequence and optional condition 


even = [x for x in range(50) if x % 2 == 0]
# the first x is an output expression 
# x after for is a member of sequence
# range(50) is an input sequence 
# x % 2 is optional condition
print(even)

vowels = "aeiou"
string = "This is a string, I want vowels" 
only_vowels = [letter for letter in string if letter in vowels]
print(only_vowels)
no_vowels = [letter for letter in string if letter.lower() not in vowels]
print("".join(no_vowels))