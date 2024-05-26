# РЕШУ егэ по новым
# with open('/home/student/Рабочий стол/w/26.05.2024/27-B.txt') as file:
#     n = file.readline()
#     f = sorted(list(map(int, file.readlines())))[::-1]
# a = []
# for i in f:
#     a.append([i, i%105])
# l = len(a)
# mx = -9999
# for i in range(l-2):
#     i0 = a[i][0]
#     i1 = a[i][1]
#     for j in range(i+1, l-1):
#         j0 = a[j][0]
#         j1 = a[j][1]
#         for k in range(j+1, l):
#             k0 = a[k][0]
#             k1 = a[k][1]
#             if (k1+j1+i1) % 105 == 0:
#                 mx = max(k0+j0+i0, mx)
#                 break
# print(mx)


# with open('/home/student/Рабочий стол/w/26.05.2024/27-A_4.txt') as file:
#     k = 2 * int(file.readline())
#     n = int(file.readline())
#     f = list(map(int, file.readlines()))

# lst = []
# for x in range(n):
#     for y in range(x + 1, n):
#         for z in range(y + 1, n):
#             if (y-x) == k or (z - x) == k or (z - y) == k:
#                 lst.append(f[x] + f[y] + f[z])
# print(max(lst))

# with open('/home/student/Рабочий стол/w/26.05.2024/27_A_8_2024.txt') as file:
#     k = int(file.readline())
#     n = int(file.readline())
#     f = list(map(int, file.readlines()))

# lst = []
# for x in range(n):
#     for y in range(x + 1, n):
#         for z in range(y + 1, n):
#             if (y-x) >= k and (z - x) >= k and (z - y) >= k:
#                 lst.append(f[x] + f[y] + f[z])
# print(max(lst))

# with open('/home/student/Рабочий стол/w/26.05.2024/1_27_A_1.txt') as file:
#     n = int(file.readline())
#     f = list(map(int, file.readlines()))


# lst = []
# for j in range(n):
#     s = 0
#     for i in range(n):
#         s = s + f[i] * min(i, n - i)
#     lst.append(s)
#     t = f[0]
#     for k in range(n - 1):
#         f[k] = f[k + 1]
#     f[-1] = t
# print(min(lst))

# КПОЛЯКОВ
# with open('/home/student/Рабочий стол/w/26.05.2024/27-a_7112.txt') as file:
#     n = int(file.readline())
#     f = list(map(int, file.readlines()))
# a = f[:n]
# b = f[n:]
# mn = 99999
# for i in a:
#     for j in b:
#         mn = min(mn, abs(j - i))
# print(mn)


with open('/home/student/Рабочий стол/w/26.05.2024/27-b_7111.txt') as file:
    n = int(file.readline())
    f = list(map(int, file.readlines()))


cnt = 0
for i in range(n):
    s = int(f[i] > 0) - int(f[i] < 0)
    if s == 0:
            cnt += 1
    for j in range(i + 1, n):
        s += int(f[j] > 0) - int(f[j] < 0)
        if s == 0:
            cnt += 1
print(cnt)