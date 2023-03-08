import numpy as np

PHI = (1 + 5 ** 0.5) / 2

def func(x):
    return x ** 3 - 2 * x - 5


def bi_sect(func, a, b, eps, max_iters) -> float:
    """
    Метод Дихотомии
    """
    c: float = .0
    if a > b:
        a, b = b, a

    cnt: int = 0

    for cnt in range(max_iters):

        c = (a + b) * 0.5

        if func(c + eps) > func(c - eps):
            b = c
        else:
            a = c

        if abs(b - a) < eps:
            break

    print('Кол-во итераций:', cnt)

    return (a + b) * .5


def golden_ratio(func, a, b, eps, max_iters):
    """
    Метод Золотого сечения
    """
    c: float = .0
    if a > b:
        a, b = b, a

    cnt: int = 0

    for cnt in range(max_iters):

        x1 = b - (b - a) / PHI
        x2 = a + (b - a) / PHI

        if func(x1) >= func(x2):
            a = x1
        else:
            b = x2

        if abs(a - b) < eps:
            break

    print('Кол-во итераций:', cnt)

    return (a + b) * .5


def fibonacci(n):
    if n < 1:
        return 0, 0
    if n < 2:
        return 0, 1
    prev_num = 0
    num = 1
    while n > num:
        prev_num, num = num, num + prev_num
    return prev_num, num


def fib(func, a, b, eps, max_iters):
    """
       Метод Фибоначчи
    """


    if a > b:
        a, b = b, a

    f_n, f_n_1 = fibonacci((b - a) / eps)

    while f_n_1 != f_n:
        d = b - a
        if abs(d) < eps:
            break
        f_tmp = f_n_1 - f_n # Число Фибоначчи f(n - 1)

        x1 = a + d * f_tmp / f_n_1
        x2 = a + d * f_n / f_n_1

        f_n_1 = f_n # сдвигаем влево
        f_n = f_tmp
        if func(x1) > func(x2):
            a = x1
        else:
            b = x2

    return (a + b) * .5

asw = fib(func, -10, 10, 0.000001, 100)
print(asw)
