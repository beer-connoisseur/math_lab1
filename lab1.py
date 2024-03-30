import matplotlib.pyplot as plt
import numpy as np
import random

def f(x):           #задаем функцию
    return 2**x

def base(arg, x1, x2): #функция, которая задает оснащение в зависимости от метода
    if arg == 1:
        return x1
    if arg == 2:
        return x2
    if arg == 3:
        return x1 + (x2 - x1) / 2
    if arg == 4:
        return random.uniform(x1, x2)

def main():
    print("нижний предел интегрирования:")
    bottom = int(input())
    
    print("верхний предел интегрирования:")
    top = int(input())
    
    if bottom >= top:
        print("некорректно введены данные")
        return 1
    
    print("число точек разбиения:")
    n = int(input())

    if n < 2:
        print("вы ввели некорректное значение")
        return 1
    
    print("способ выбора оснащения:\n1.левые\n2.правые\n3.средние\n4.случайные")
    arg = int(input())     
    if not(arg == 1 or arg == 2 or arg == 3 or arg == 4):
        print("вы ввели некорректное значение")
        return 1

    x = np.linspace(bottom, top, 100) #рисуем график 2**x
    plt.plot(x, f(x))

    x1 = 0
    x2 = 0
    res = 0
    t = (top - bottom) / (n - 1) #задаем величину промежутка между точками разбиения(разбиение равномерное)
    for i in range(n-1): #строим прямоугольники в зависимости от выбранного метода
        x2 = x1 + t
        plt.bar(x1, f(base(arg, x1, x2)), x2 - x1, 0, align="edge", color="white", edgecolor="black") #plt.bar(начало по х, высота столбца, ширина столбца, начало по у, выравнивание по краю)
        res += f(base(arg, x1, x2)) * (x2 - x1)
        x1 = x2
    res = round(res, 3)
    plt.text(0, f(top), "площадь под графиком равна", fontdict=None)
    plt.text(0, f(top) - f(top)/10, res, fontdict=None)
    plt.show()
    print("площадь под графиком равна:", res)

if __name__ == "__main__":
    main()

