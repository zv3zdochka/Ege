
with open('1.txt', 'r') as f:
    data = f.readline()
    print(len(data))
    s_i = 0
    lens = []
    while s_i <= len(data) -2:
        if s_i % 1000 == 0:
            print(s_i)
        s = ''
        for i in data[s_i:]:
            s += i
            if s.count('.') <= 3:
                continue
            else:
                lens.append(len(s))

                break
        s_i += 1
    print(max(lens)-1)