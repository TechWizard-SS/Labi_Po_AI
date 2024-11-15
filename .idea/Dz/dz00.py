import math
def xxx(x):
        result = math.sqrt(3 * x - 1) + (1 + x)**2
        return result

x = float(input("Введите значение x: "))
result = xxx(x)
print(f"Результат вычисления: {result}")