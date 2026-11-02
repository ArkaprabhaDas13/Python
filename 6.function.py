def myFunc(a, b):
    return "Arka", a+b

ans = myFunc(4, 6)

print(ans)
print(type(ans))


def greet(name="Arkaprabha"):
    print(f"My name is {name}")

greet("Rock")

def add(*nums):
    add = 0
    print(nums)
    for i in nums:
        add = add+i
    return add

sum = add(1,2,3,4,5,6)

print(sum)

def myAdd(**kwargs):
    print(kwargs)

result = myAdd(name="Arka", age=25, location="Kolkata")
print("result = ", result)

def test(a, b, c):
    print(f"test output = {a} {b} {c}")

nums = [1,2,3]

test(*nums)