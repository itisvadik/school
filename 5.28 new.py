for i in range(100, 1, -1):
    n = bin(i)[2:]
    n = str(n)
    if i % 2 == 0:
        n += '00'
    else:
        n += '11'
    r = int(n, 2)
    if r <= 134:
        print(i)
        break
