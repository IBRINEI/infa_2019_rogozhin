from math import sin, cos, pi


def prime(a):
    m = []
    m.append(2)
    n = 0
    q = True
    for i in range(a):
        for j in range(n):
            if (i + 3) % m[j] == 0:
                q = False
        if q:
            m.append(i + 3)
            n = n + 1
        else:
            q = True
    print(m)


def sort(m):
    q = 0
    for i in range(len(m)):
        for j in range(len(m) - i):
            if m[j + i] < m[q]:
                q = j + i
        m[i], m[q] = m[q], m[i]
        q = i + 1
    print(m)


def rotate_square(square, angle):
    mid_x = 0
    mid_y = 0
    square1 = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(4):
        mid_x = mid_x + square[i][0]
        mid_y = mid_y + square[i][1]
    for i in range(4):
        square1[i][0] = (square[i][0] - mid_x/4)*cos(angle) - (square[i][1] - mid_y/4)*sin(angle) + mid_x/4
        square1[i][1] = (square[i][0] - mid_x/4)*sin(angle) + (square[i][1] - mid_y/4)*cos(angle) + mid_y/4
        square1[i] = tuple(square1[i])
    print(square1)


def market(lst, money):
    m = []
    for key in lst:
        if lst[key] < money:
            m.append(key)
    print(m)

def no_duble(m):
    set1 = set(m)
    print(list(set1))

def difference(m1, m2):
    q = True
    m3 = []
    for i in m1:
        for j in m2:
            if i == j:
                q = False
        if q:
            m3.append(i)
        else:
            q = True
    print(list(set(m3)))

prime(1000)
sort([6, 4, 2, 5, 35, 3, 34, 25, 0])
rotate_square(((1, 1), (1, -1), (-1, -1), (-1, 1)), pi)
market({'banana': 11, 'apple': 5, 'steak': 100}, 50)
no_duble([1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5])
difference([1, 2, 3, 2], [3, 4])

