def do(a):
    a1 = str(bin(a))[2:]
    n = 0
    for i in a1:
        n += int(i)
    n1 = a1 + str(n % 2)

    f = 0
    for i in n1:
        f += int(i)
    n2 = n1 + str(f % 2)

    return int(n2, 2)
print(do(5))

i = 1
while True:
    if do(i) > 93:
        print((do(i)))
        break
    else:
        i += 1