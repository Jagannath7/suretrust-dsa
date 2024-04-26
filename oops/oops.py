#
#
# class Student:
#     counter = 1
#     def __init__(self, name ):
#         self.name = name
#         self.roll = Student.counter
#         Student.counter += 1
#
#     def __str__(self):
#         return f'name is {self.name} and roll no is {self.roll}'
#
#
# s1 = Student('A')
# s2 = Student('B')
# s3 = Student('C')
#
#
# print(s1)
#
# print(s2)
# print(s3)



class Account:
    counter = 1
    def __init__(self, bal = 0):
        self.__bal = bal
        self.id = Account.counter
        Account.counter += 1

    def __str__(self):

        return f'bal is {self.bal}'

    def deposit(self, amount):

        if amount > 0:
            self.__bal += amount

    def withdraw(self, amount):

        if amount > 0 and amount < self.__bal:

            self.__bal -= amount

    def getBal(self):
        return self.__bal

    def getInterest(self):
        return self.getBal() * 0.07

class SavingsAccount(Account):

    def getInterest(self):

        return super().getInterest()




s1 = SavingsAccount(100)

print(s1.getInterest())




















