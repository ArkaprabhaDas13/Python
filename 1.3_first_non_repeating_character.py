# Find the first non-repeating character in a string

dict = {}

str = "aaaapple"

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict.get(i)+1

for key, value in dict.items():
    if value == 1:
        print(key)
        break

