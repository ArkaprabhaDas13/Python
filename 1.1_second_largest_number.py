nums = [1,2,3,4,5,6,7,8,5,3,1]

max = None
second = None

for i in nums:
    if max is None or i > max:
        second = max
        max = i
    elif second is None or i > second:
        second = i

print(max)
print(second)
        


# 20 3 10 5

# largest = None 20

# second_largest = None