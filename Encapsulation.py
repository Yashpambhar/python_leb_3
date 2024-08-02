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
