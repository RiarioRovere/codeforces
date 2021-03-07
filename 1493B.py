t = int(input())

def h_isok(h1, m):
    if set(str(h1)).issubset({'0', '1', '2', '5', '8'}) and int(str(h1).zfill(2)[::-1]) < m:
        return 1
    return 0

def m_isok(m1, h):
    if set(str(m1)).issubset({'0', '1', '2', '5', '8'}) and int(str(m1).zfill(2)[::-1]) < h:
        return 1
    return 0

def print_time(h1, m1):
    print(str(h1).zfill(2) + ':' + str(m1).zfill(2))

for i in range(t):
    h, m = map(int, input().split())
    h1, m1 = map(int, input().split(':'))

    while not h_isok(h1, m):
        h1 = (h1 + 1) % h

    while not m_isok(m1, h):
        m1 = (m1 + 1) % m

    print_time(h1, m1)
