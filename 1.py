# from itertools import product


# def f(x, y, z, w):
#     return int((x and (not z)) or (y == z) or (not w)) == 1


# for x, y, z, w in product([0, 1], repeat=4):
#     if not f(x, y, z, w):
#         print(w, y, z, x)


# def f(n):
#     r = f'{n:b}'
#     if n % 2 == 0:
#         r += '01'
#     else:
#         r = '1' + r + '1'
#     r = int(r, 2)
#     return r > 156


# for i in range(1000):
#     if f(i):
#         print(i)
#         break

# from turtle import *

# lt(90)
# tracer(0)
# screensize(10000, 10000)

# m = 20

# down()
# for _ in range(2):
#     fd(13 * m )
#     rt(90)
#     fd(18 * m )
#     rt(90)
# up()
# fd(5 * m )
# rt(90)
# fd(9 * m )
# lt(90)
# down()
# for _ in range(2):
#     fd(11 * m )
#     rt(90)
#     fd(7 * m )
#     rt(90)
# up()

# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x*m, y*m)
#         dot('blue')

# done()
# print(9 * 8)

# print(2 ** 13)
# print(2764 * 1793 * 13 * 148 / 18349566)


# from itertools import product

# c = 0
# for a in product(sorted('ПАРУС'), repeat=5):
#     s = ''.join(a)
#     c += 1
#     if 'АА' not in s and s.count('У') <= 1:
#         print(c)
#         break

# cnt = 0
# with open('/home/student/Рабочий стол/w/9_15321.csv') as file:
#     f = file.readlines()
#     for i in f:
#         a, b, c, d = i.split(';')
#         s = sorted([int(a), int(b), int(c), int(d)])
#         mx = s[-1]
#         if mx < sum(map(int, s[::-1])):
#             sums = [a + b, a + c, a + d, b + c, b + d, d + d]
#             t = False
#             for g in range(len(sums) - 1):
#                 k1 = sums[g]
#                 for u in range(g + 1, len(sums)):
#                     k2 = sums[u]
#                     if k1 == k2:
#                         t = True
#                         break
#             if t:
#                 cnt += 1
# print(cnt)
        


# print(22528 / 1024 * 9)

# a = 45 * '8'

# while '1111' in a or '8888' in a:
#     if '1111' in a:
#         a = a.replace('1111', '88', 1)
#     else:
#         a = a.replace('8888', '11', 1)
# print(a) 

# from itertools import product

# cnt = 0
# for w in range(0, 255):
#     if w & 224 == 224:
#         s = f'{w:b}'.count('1')
#         if (10 + s) % 4 == 0:
#             cnt += 1
# print(cnt)

# from string import ascii_uppercase

# def f(n, k=27):
#     a = '0123456789' + ascii_uppercase
#     s = 0
#     while n > 0:
#         if n % k > 10:
#             s+=1
#         n //= k
#     return s
# w = 3 * 2187**2020 + 3 * 729 ** 2021 - 2 * 81 ** 2022 + 27 ** 2023 - 4 * 3 ** 2024 - 2029
# print(f(w))


# from string import ascii_uppercase

# for x in range(26, -1, -1):
#     b = '0123456789' + ascii_uppercase
#     q = int(f'123{b[x]}24', 27) + int(f'135{b[x]}78', 27)
#     if q % 26 == 0:
#         print(q / 26)



# def f(a):
#     for x in range(500):
#         if int((not(x%a==0)) <= ((x%28==0) <= (not(x%49==0)))) == 0:
#             return False
#     return True

# for A in range(10000, 1, -1):
#     if f(A):
#         print(A)
#         break

# from itertools import product



# def f(A):
#     B = [i for i in range(24, 91)]
#     C = [i for i in range(47, 116)]
#     for x in range(500):
#         if int((x in C) <= (((not(x in A)) and (x in B)) <= (not(x in C)))) == 0:
#             return False
#     return True

# s = []
# for a in range(200):
#     for b in range(a + 1, 200):
#         a0 = [i for i in range(a, b+1)]
#         if f(a0):
#             s.append(b-a)
# print(min(s))


a = 0
cnt = 0
with open('/home/student/Рабочий стол/w/24_15339.txt') as file:
    f = file.readline()
    t = False
    f = f.replace('A', 'L').replace('B', 'L').replace('C', 'L').replace('6', '1').replace('7', '1').replace('8', '1'). replace('9', '1')
    for i in range(len(f)-1):
        if f[i]+f[i+1] not in ['AA', '11']:
            cnt += 1
            t = True
        elif t:
            a = max(cnt, 0)
            cnt = 0
            t = False
print(a)