# Check whether two strings are anagrams

str1 = "sillent"
str2 = "listen"

dict = {}

for i in str1:
    if i not in dict:
        dict[i] = 1
    else:
        print("Not an anagram")
        exit()

for i in str2:
    if i not in dict:
        print("Not an anagram")
        exit()
    else:
        dict[i] = dict.get(i)-1


count = 0
for value in dict.values():
    if value != 0:
        count = count+1

if count == 0:
    print("Anagram")
else:
    print("Not an Anagram")