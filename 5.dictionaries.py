myDict = {
    "name": "Arka",
    "age": 35
}

print(myDict["name"]);
print(myDict["age"]);

myDict["city"] = "Howrah"


myDict.pop("age")
print(myDict)

jobVal = myDict.get("job", "Unknown")
print(jobVal)

print(myDict.keys())

print(myDict.values())


for key, value in myDict.items():
    print(key, " - ", value)

print(myDict.get("loc"))

