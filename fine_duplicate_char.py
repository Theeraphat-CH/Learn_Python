"""
def find_dup_chars(input):
    duplicate = {}
    for char in input:
        if char in duplicate:
            duplicate[char] += 1
        else:
            duplicate[char] = 1
    for char in duplicate:
        if duplicate[char] > 1:
            print(char)
            print(duplicate)

find_dup_chars("maximum occurrence")
"""
#Get string and integer values and group
dict_of_chars = {}

#Get string
char = input("Enter a character : ")

for i in char:
    if i in dict_of_chars:
        dict_of_chars[i] += 1
    else:
        dict_of_chars[i] = 1

for i in dict_of_chars:
    if dict_of_chars[i] > 1:
        print(i)



