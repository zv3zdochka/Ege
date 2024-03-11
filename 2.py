def imp(a,b): return a <= b

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = y and (imp(x,w)) and (imp(not x, (not w == z)))
                if not f:
                    print(x,y,z,w)