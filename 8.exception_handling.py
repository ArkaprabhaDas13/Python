num = 20

# try:
#     print(num/0)
# except:
#     print("division by zero not allowed")


# obj = {
#     "name" : "Arkaprabha"
# }
# try:
#     print(obj["age"])
#     res = 10/0
# except ZeroDivisionError:
#     print("Division by zero")
# except:
#     print("error")

# int("String")

dict = {
    "name": "arkaprabha"
}

# print(dict["age"])


age = 20
try:
    if(age<1):
        raise ValueError("Age cannot be negetive or zero")
    zero = num/0
except ZeroDivisionError as e:
    print("Division by Zero", e)
else:
    print("call the api")
finally:
    print("I will always run!")