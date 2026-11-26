import math

class AreaCalc:
    def calculate(self, length: float, width: float = None) -> float:
        if not width:
            return round(math.pi * length**2, 2)
        else:
            return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
