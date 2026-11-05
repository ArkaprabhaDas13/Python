# Write a function that groups words by their first character

list = ['apple', 'mango', 'ace', 'house', 'howrah', 'cat', 'comfortable']

dict = {}
def group(list):
    for i in list:
        if i[0] not in dict:
            dict[i[0]] = [i]
        else:
            dict[i[0]].append(i)

group(list)

print(dict)