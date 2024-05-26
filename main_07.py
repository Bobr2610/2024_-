# from turtle import *

# lt(90)
# tracer(0)
# screensize(10000, 10000)

# m = 40

# rt(60)
# for _ in range(2):
#     fd(10 * m )
#     rt(120)
#     fd(5 * m )
#     rt(240)
# rt(120)
# fd(3 * m)
# rt(90)
# fd(20*(3**0.5) * m )
# rt(90)
# fd(8 * m )
# rt(120)
# for _ in range(2):
#     fd(10 * m )
#     lt(120)
#     fd(5 * m )
#     lt(240)

# up()

# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x*m, y*m)
#         dot('blue')

# done()

# from turtle import *

# lt(90)
# tracer(0)
# screensize(10000, 10000)

# m = 40

# rt(180)
# fd(5 * m)
# rt(90)
# fd(50 * m)
# rt(90)
# fd(5 * m) 

# for _ in range(5):
#     seth(90)
#     circle(-5 * m, 180)

# up()

# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x*m, y*m)
#         dot('blue')

# done()

# from ipaddress import *

# cnt = 0

# for A in range(256):
#     ip = f'246.81.65.{A}'
#     net = ip_network(f'{ip}/255.255.255.224')

#     if ip not in (net.network_address, net.broadcast_address):
#         if all(f'{ip:b}'[16:24].count('0') > f'{ip:b}'[24:].count('0') for ip in net.hosts()):
#             cnt += 1
# print(cnt)

# g_o = 777


# def f(x1, x2, c, pob):
#     if x1 * x2 >= g_o or c > max(pob):
#         return c in pob
#     moves = [f(x1 + 3, x2, c + 1, pob), f(x1 * 2, x2, c + 1, pob), f(x1, x2 + 3, c + 1, pob), f(x1, x2 * 2, c + 1, pob)]
#     if c % 2 == max(pob) % 2:
#         return all(moves)
#     else:
#         return any(moves)


# print('\n#19')
# for s in range(1, 111):
#     if not f(7, s, 0, [1]) and f(7, s, 0, [2]):
#         print(s)
#         break

# print('\n#20')
# for s in range(1, g_o + 1):
#     if not f(7, s, 0, [1]) and f(7, s, 0, [3]):
#         print(s)


# print('\n#21')
# for s in range(1, g_o + 1):
#     if f(7, s, 0, [2, 4]) and not f(7, s, 0, [2]):
#         print(s)
#         break

# def f(n, k, t):
#     if n > k or t > 2:  
#         return 0
#     if n == k:
#         return 1
#     return f(n - 2, k, t + 1) + f(n * 2, k, t) + f(n * 3, k, t)

# print(f(6, 48, 0))

