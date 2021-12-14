s = '1' * 61



def F(s):
    while '111' in s:
        s.replace('111', '2', 1)
        if '222' in s:
            s.replace('222', '11', 1)
    return s


for i in range(60, 100):
    x = '1' * i
    print(F(x))
