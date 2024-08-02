class Calculator:
    def _init_(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

calc = Calculator(10, 5)

result_addition = calc.add()
result_subtraction = calc.subtract()

print("Addition Result:", result_addition)
print("Subtraction Result:", result_subtraction)

output :-
![pro5](https://github.com/user-attachments/assets/20b930db-ab42-4e7e-ba7f-4a42cb456cf1)
