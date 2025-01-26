import numpy
import time

def measure(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(end - start)
    return wrapper

m = [int(x) for x in range(100_000_000)]
s = set(m)

@measure
def Using_set(s):
    if 77_777_777 in s:
        print("Set found")

@measure
def Using_list(m):
    if 77_777_777 in s:
        print("List found")

Using_list(m)
Using_set(s)