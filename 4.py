from string import ascii_uppercase, digits


l = list(digits+ascii_uppercase)


def to_ss(a,n):
    s = ''
    while a >= n:
        s += str(a % n)
        a = a // n
    s += l[a]
    s = s[::-1]
    print(s)

print(to_ss(225, 16))