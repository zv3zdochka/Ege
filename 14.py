# var 1
from string import digits, ascii_uppercase

alls = list(digits + ascii_uppercase)
N = 22
a = "98x79641"
b = "36x14"
c = "73x4"
n = []
for i in alls[:N]:
    f = int(a.replace("x", str(i)), N) + int(b.replace("x", str(i)), N) + int(c.replace("x", str(i)), N)
    if f % 21 == 0:
        n.append([i, f / 21])
print(n)

# var 2 27301
from string import ascii_uppercase

SS = 25
n = 16 ** 4 + 8 ** 4 + 4 ** 6 - 64
print(n)
string = ''
while n > 0:
    ost = n % SS
    if ost >= 10:
        ost = ascii_uppercase[ost - 10]
    string += str(ost)
    n //= SS
print(string[::-1])

# var 3 48381
from string import digits, ascii_uppercase

all = list(digits + ascii_uppercase)
print(all)
N = 14
m = "8x12x"
n = "8x542"
h = []
for a in range(0, 1000):
    for x in all[:N]:
        x = str(x)
        if (int(m.replace("x", x), N) + a) % int(n.replace("x", x), N) == 0:
            h.append((a, x))
print(h)

# var 4 48398

h = []
a = 'xB09'  # в 17-ричной
b = 'x8E8'  # в 15-ричной
# x из десятичной сс
for x in range(0, 10):
    f = int(a.replace('x', str(x)), 17) + int(b.replace('x', str(x)), 15)
    if f % 155 == 0:
        h.append((x, f / 155))
print(h)

# var 5 48391

from string import digits, ascii_uppercase

alle = list(digits + ascii_uppercase)

h = []
a = 'yAAx'  # в 12-ричной
b = 'x02y'  # в 14-ричной
# x,y в пределах допустимых сс
for x in alle[:12]:
    for y in alle[:12]:
        f = int(a.replace('x', str(x)).replace('y', str(y)), 12) + int(b.replace('x', str(x)).replace('y', str(y)), 14)
        if f % 80 == 0:
            h.append((x, y, f / 80))
print(h)

# var 52185
from string import digits, ascii_uppercase

all = list(digits + ascii_uppercase + ':')
print(all)


def conv(number: str, num_sys: int):
    l = len(number) - 1
    num = 0
    for i in number:
        if i.isdigit():
            num += num_sys ** l * int(i)
            l -= 1
        else:
            k = all.index(i)
            num += num_sys ** l * int(k)
            l -= 1
    return num


N = 37
m = "317x"
n = "4x29"
h = []
for x in all:
    f = conv(m.replace('x', str(x)), N) + conv(n.replace('x', str(x)), N)
    if f % 36 == 0:
        h.append((x, f / 36))
print(h)
