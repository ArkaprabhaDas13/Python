class User:
    name = "John Doe"
    age = 18
    def greet(self):
        print(f"hello {self.name}")

user1 = User()


user1.name = "ARkaprabha"
print(user1.name)

user1.greet()