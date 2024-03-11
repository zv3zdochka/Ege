import itertools

al = "БОРИС"
li = (itertools.product(al, repeat=6))
zu = []
for i in li:
    zu.append(i)
print(zu)
co = 0
for j in zu:
    if j.count("Б") == 1 and j.count("Р") == 1 and j.count("С") <= 1:
        co += 1
print(co)

from itertools import *

z = []
for i in product(sorted("ЦИТРУС"), repeat=5):
    s = list(i)
    print(s, list(product(sorted("ЦИТРУС"), repeat=5)).index(i))
