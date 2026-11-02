num = {1,2,2,4,5,6}
num2 = {3,4,5,7,8}

num.add(100)
# num.pop()
num.discard(400)
# num.remove(300)

newSet = num.union(num2)
print(newSet)

newSet2 = num.intersection(num2)
print(newSet2)