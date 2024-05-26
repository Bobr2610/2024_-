# from itertools import product


# def f(a, b, c, d):
#     return ((a <= b) and (b <= (not c)) and ((not c) <= d))
#  

# for a, b, c, d in product([0, 1], repeat=4):
#     if f(a, b, c, d):
#         print(d, c, b, a)

# def f(n, k):
#     s = ''
#     while n > 0:
#         s += str(n % k)
#         n //= k
#     return s[::-1]

# mn = 99999
# for n in range(1, 10000):
#     r = f(n, 3)
#     if n % 2 == 0:
#         r = '2' + r + f(int(r[-1], 3)*2, 3)
#     else:
#         r = f(int(r[0], 3)*2, 3) + r + '2'
#     r = int(r, 3)
#     if r > 100:
#         mn = min(mn, r)
# print(mn)


# from itertools import product


# cnt = 0
# for x in product('012345678', repeat=7):
#     s = ''.join(x)
#     if (s[0] in '2468') and (s[-1] in '124578') and (s.count('6') > 0):
#         cnt += 1
# print(cnt)


# with open('/home/student/Рабочий стол/w/19_05_2024/files/09_16256.csv') as file:
#     f = file.readlines()
#     for i in f():
#         s = list(map(int, i.split(';')))
#         if len(set(s)) == 2:


# print((120 * 1024 / 1536 ) - 48)
# print(32 * 8 / 35)
# print(2 ** 7)


from itertools import permutations



def f(n):
    while '3' in n:
        n = n.replace('342', '4123')
        n = n.replace('34', '413')
        n = n.replace('32', '13')
        n = n.replace('33', '424')
    return sum(map(int, n))


mx = -9999
for x in permutations('4' * 40 + '2' * 25):
    s = ''.join(x) + '3'
    mx = max(mx, f(s))
print(mx)