def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 3, y)
print(f(4, 34))