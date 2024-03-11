from random import shuffle
s = list('7'*40 + '9' * 40 + '4' * 50)
shuffle(s)
s = ''.join(s)
while '49' in s or '97' in s or '47' in s:
    if '47' in s:
        s = s.replace('47', '74', 1)
    elif '97' in s:
        s = s.replace('97', '79', 1)
    elif '49' in s:
        s = s.replace('49', '94', 1)
print(s[24] + s[70] + s[104])