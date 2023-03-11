PHI = (1 + 5 ** 0.5) * .5


def func(x):
    return x ** 2 - 3 * x + 2


def bi_sect(func, a, b, eps, max_iters) -> float:
    """
    Метод Дихотомии
    """
    c: float = .0

    if a > b:
        a, b = b, a

    cnt: int = 0

    for cnt in range(max_iters):

        c = (a + b) * .5

        if func(c + eps) > func(c - eps):
            b = c
        else:
            a = c

        if (b - a) < eps:
            break

    print('Кол-во итераций:', cnt)

    return (a + b) * .5


def golden_ratio(func, a, b, eps, max_iters) -> float:
    """
    Метод Золотого сечения

    """

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


def fib(func, a, b, eps):
    """
       Метод Фибоначчи
    """

    if a > b:
        a, b = b, a

    f_n, f_n_p_1 = fibonacci((b - a) / eps)

    cnt: int = 0

    while f_n_p_1 != f_n:
        cnt += 1

        d = b - a

        if abs(d) < eps:
            break

        f_n_m_1 = f_n_p_1 - f_n

        x1 = a + d * f_n_m_1 / f_n_p_1
        x2 = a + d * f_n / f_n_p_1

        f_n_p_1 = f_n
        f_n = f_n_m_1

        if func(x1) > func(x2):
            a = x1
        else:
            b = x2

    print('Кол-во итераций:', cnt)

    return (a + b) * .5


print(bi_sect(func, -3, 3, 0.000001, 100), golden_ratio(func, -3, 3, 0.000001, 100), fib(func, -3, 3, 0.000001))
