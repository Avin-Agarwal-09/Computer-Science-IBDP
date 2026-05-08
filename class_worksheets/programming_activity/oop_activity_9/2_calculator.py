class Calculator:
    def add(self, a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
        return result

calc = Calculator()
calc.add(5, 10)
calc.add(5.5, 4.5)