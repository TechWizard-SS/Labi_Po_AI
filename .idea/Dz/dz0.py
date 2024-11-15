import math
def calculate_expression(x):
    try:
        result = math.sqrt(3 * x - 1) + (1 + x)**2
        return result
    except ValueError:
        return "Недопустимое значение x. Выражение под корнем должно быть неотрицательным."


x = float(input("Введите значение x: "))
result = calculate_expression(x)
print(f"Результат вычисления: {result}")