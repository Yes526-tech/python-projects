class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    def deposit(self, amount):
        self.amount = amount
        new_money = self.balance + amount
        self.balance = new_money
        return self.balance

    def withdraw(self, amount):
        self.amount = amount
        new_money = self.balance - amount
        self.balance = new_money
        return self.balance


person1 = BankAccount("Yunus")
person1.deposit(1000)
print(person1.balance)
print(person1.owner)