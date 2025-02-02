import math
import time

"""
def height(n,m):
    f = math.factorial(m)
    facs = [math.factorial(x) for x in range(m, 0, -1)]
    return sum(f//(facs[x] * math.factorial(x)) for x in range(1, n + 1)) if n and m > 0 else 0
"""
"""
def height(n,m):
    res = 0
    f = math.factorial(m)
    g = f
    k = 1
    for x in range(1, n + 1):
        g = g // (m - x + 1)
        k = k*x
        res += f//(g * k)
"""

def height(n,m):
    if m == 0 or n == 0:
        return 0

    f = math.factorial(m)

    res = f//(f//m)
    fac = f//(f//m)

    for x in range(2, n + 1):
        fac = fac*(m - x + 1)//(x)
        res += fac

    return res


start = time.time()
print(height(7,20))
print(height(9477,10000))
end = time.time()
print(end - start)