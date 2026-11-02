old = [1,2,3,4,5]

new = [num*num for num in old]

print(new)

newEven = [num*num for num in old if num%2 == 0]

print(newEven)

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num for row in matrix for num in row]

print("Flattened matrix = ", flat)

numbers = [1,2,3,4,5,6]

squares = {num: num*num for num in numbers}

print("squares = ", squares)