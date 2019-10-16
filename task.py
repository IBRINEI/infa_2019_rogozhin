from math import sin, cos, pi


# Makes a list of all prime numbers that a not more than a
def prime(a):
    m = [2]
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
    return m


# Sorting function; "Selection sort" (in - list)
def sort(m):
    q = 0
    for i in range(len(m)):
        for j in range(len(m) - i):
            if m[j + i] < m[q]:
                q = j + i
        m[i], m[q] = m[q], m[i]
        q = i + 1
    return m


# Prints a list of tuples of coordinates of a turned square based on starting coordinates and angle
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
    return square1


# You can buy everything that will be printed (in - set of items {'item' : price}; your money)
def market(dct, money):
    m = []
    for key in dct:
        if dct[key] < money:
            m.append(key)
    return m


# Removes all the dubles that appear in inserted list
def no_duble(m):
    return list(set(m))


# Mathematical difference of sets, that are inserted as two lists
def difference(m1, m2):
    return (set(m1)).difference(set(m2))


print(prime(1000))
print(sort([6, 4, 2, 5, 35, 3, 34, 25, 0]))
print(rotate_square(((1, 1), (1, -1), (-1, -1), (-1, 1)), pi))
print(market({'banana': 11, 'apple': 5, 'steak': 100}, 50))
print(no_duble([1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5]))
print(difference([1, 2, 3, 2], [3, 4]))
