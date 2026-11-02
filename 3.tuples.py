# non mutable

tuple = (1, "Arka", 5)

print(tuple)
print(tuple[0])

rank, name, userid = tuple
# print(name)

rank, name = name, rank


print(rank)


myTuple = (30,)

print(type(myTuple))