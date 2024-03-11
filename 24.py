def do(st: str):
    m_l = 0
    li = 0
    flag = 0
    for i in st:
        if i == "C":
            flag = 1
            li += 1
            if li > m_l:
                m_l = li
        else:
            flag = 0
            li = 0
    return m_l


with open('br.txt', 'r') as f:
    l = f.readline()
    print(do(l))


# /////////////////////////////////////////////////
def doh(st: str):
    st = st.replace("A", '').replace("B", '').split()
    print(sorted(st))



with open('br.txt', 'r') as f:
    l = f.readline()
    print(doh(l))


#///////////////////////////////////////////////////////

a = open("br.txt", 'r')
text = a.readline()
text = 'D '

def do():
    global max_len, cur_len
    if cur_len > max_len:
        max_len = cur_len


max_len = 0
cur_len = 0
flag = 0
for i in text:
    if i == 'D':
        cur_len += 1
        do()
        flag = 1
        continue
    if i == 'B' and flag == 1:
        cur_len += 1
        do()
        flag = 2
        continue
    if i == 'A' and flag == 2:
        cur_len += 1
        do()
        flag = 3
        continue
    if i == 'C' and flag == 3:
        cur_len += 1
        do()
        flag = 4
        continue
    if i == 'D' and flag == 4:
        cur_len += 1
        do()
        flag = 0
        continue

    else:
        cur_len = 0
print(max_len)

with open('br.txt', 'r') as file:
    m_l = 0
    cur_l = 0
    a = file.readline()
    for i in a:
        if i == 'B' or i == 'E' or i == 'F':
            if cur_l > m_l:
                m_l = cur_l
            cur_l = 0
        else:
            cur_l += 1
            if cur_l > m_l:
                m_l = cur_l
    print(m_l)


with open('br.txt', 'r') as file:
    m_l = 0
    cur_l = 0
    a = file.readline()
    z = [i.split('E') for i in a.split('D')]
    m_l = 0
    for i in z:
        if len(max(i)) > m_l:
            m_l = len(max(i))
    print(m_l)

with open('br.txt', 'r') as file:
    m_l = 0
    cur_l = 0
    a = file.readline()
    li = []
    for i in a.split('B'):
        if len(i.split('E')) > 1:
            for f in i.split('E'):
                li.append(f)
        else:
            li.append(i)

    k = []
    for j in li:
        if len(j.split('F')) > 1:
            for h in j.split('F'):
                k.append(h)
        else:
            k.append(''.join(j.split('F')))


    m_l = 0
    for i in k:
        if len(i) > m_l:
            m_l = len((i))
    print(m_l)


import re

# Чтение текстового файла
with open("k7b-3.txt", "r") as file:
    text = file.read()

# Используем регулярное выражение для поиска максимальной цепочки
pattern = r"(BAFE)*"
matches = re.finditer(pattern, text)

max_chain_length = 0
for match in matches:
    chain = match.group()
    max_chain_length = max(max_chain_length, len(chain))

print("Максимальная длина цепочки:", max_chain_length)




