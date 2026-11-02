list = [2, "hello", "this world", 24.35, True]

print(list[-3])

list[-2] = 24.5555

list.append("Raju")

list.insert(1, "World")

list.extend(["black hole", "sky"])

list.append(["crow", "pegion"])

list.remove(list[len(list)-1])

list.pop(3)

newlist = [1, 2, 3, 4, 5, 6, 7]

print(newlist[::-1])

print(len(newlist))

print(5 in newlist)

print(newlist.index(4))

newlist.sort(reverse=True)

print(newlist)

newlistSoftCopy = newlist
print(newlistSoftCopy)

newlistHardCopy = newlist.copy()
newlist[0] = 100
print(newlistHardCopy)

nums = [1, 1, 0, 0, 1, 1, 1, 0]

for i in range(0, len(nums)):
    print(nums[i])


def func(a, b):
    return a*b;

print(func(3, 4))