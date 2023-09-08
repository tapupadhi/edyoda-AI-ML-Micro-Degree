# Challenge 1: Square Numbers and Return Their Sum
class Point:
    def __init__(self, x: int or float, y: int or float, z: int or float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self) -> int or float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2


p = Point(1, 3, 5)
print("Challenge1: ")
print("------------")
print(p.sq_sum())
print()


# Challenge 2: Implement a Calculator Class
class Calculator:

    def __init__(self, num1: int or float, num2: int or float) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int or float:
        return self.num1 + self.num2

    def subtract(self) -> int or float:
        return self.num2 - self.num1

    def multiply(self) -> int or float:
        return self.num1 * self.num2

    def divide(self) -> int or float:
        return self.num2 / self.num1


obj = Calculator(10, 94)
print("Challenge2: ")
print("------------")
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())
print()


# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self) -> None:
        self.__name = None
        self.__rollNumber = None

    def __get_name(self) -> str:
        return self.__name

    def __set_name(self, name: str) -> None:
        self.__name = name

    def __get_roll_number(self) -> int:
        return self.__rollNumber

    def __set_roll_number(self, roll_number: int) -> None:
        self.__rollNumber = roll_number


# Challenge 4: Implement a Banking Account & Challenge 5: Handling a Bank Account
class Account:
    def __init__(self, title: str = None, balance: int or float = 0) -> None:
        self.title = title
        self.balance = balance

    def get_balance(self) -> int or float:
        return self.balance

    def deposit(self, amount: int or float) -> None:
        self.balance += amount

    def withdrawal(self, amount: int or float) -> None:
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title: str = None, balance: int or float = 0, interest_rate: int or float = 0):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    def interest_amount(self) -> int or float:
        return self.interest_rate * self.balance / 100


sa = SavingsAccount("Ashish", 5000, 5)

print("Challenge 4 & 5: ")
print("-----------------")
sa.balance = 2000
print("before deposit   : ", sa.get_balance())
sa.deposit(500)
print("after deposit    : ", sa.get_balance())

sa.balance = 2000
print("before withdrawal: ", sa.get_balance())
sa.withdrawal(500)
print("after withdrawal : ", sa.get_balance())

sa.balance = 2000
sa.interestRate = 5
print("interest amount  :", sa.interest_amount())
