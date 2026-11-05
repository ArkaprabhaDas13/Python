# Count the frequency of each character in a string.

str = "apple"

dict = {}

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict.get(i)+1

print(dict)