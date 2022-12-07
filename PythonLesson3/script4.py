print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
dicr = b ** 2 - 4*a*c
print('Дискриминант = ' + str(dicr))
if dicr == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + dicr ** 0.5) / (2 * a)
    x2 = (-b - dicr ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))