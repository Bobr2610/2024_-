
# file = open('/home/student/Загрузки/17(5).txt')

# cnt = 0

# for string in file:
#     lst = list(map(int, string.split(';')))
#     uniq = set(lst)

#     if len(uniq) == 5:
#         sum_repeat = (sum(lst) - sum(uniq))
#         av_uniq = (sum(uniq) - sum_repeat) / 4
#         if av_uniq <= (sum_repeat*2):
#             cnt += 1

# print(cnt)

# num = 3* 343**8+ 5*49**12+7**15 - 49
# S = ''
# while num > 0:
#     S = str(num%7) + S
#     num //= 7
# print(S)
# print(bin(num)[2:].count('1'))
# print(int('11000010' , 2))

# from itertools import product 


# for x, y in product( range (9), repeat=2):
#     m = [z, a, y, x][::-1]
#     n = [8, x, 7, 2, 5][::-1]

#     for i in range(len(m)): m[i] = m[i] * (9 ** i)
#     for i in range(len(n)): n[i] = n[i] * (9 ** i)

#     if (sum(m) + sum(n)) % 29 == 0:
#       print((sum(n) + sum(m)) // 29)
#       break

# for a in range(300, 1, -1): 
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (((a<=x<=b) <= (x**2 ≤ 100)) and ((x**2 ≤ 64) <= (a<=x<=b))):
#                 k += 1
#     if k == 90_000:
#         print(a)

# for A in range(1, 300): 
#     B = True
#     for x in range(1, 300):
#              for y in range(1, 300):
#               if ((x > A) or (y > A) or (2*y + x < 110)) == 0:
#                 B = False
#     if B:
#         print(A)



# file = open('/home/student/Загрузки/17-342.txt')
# file = [int(i) for i in file]

# lst = []

# lst_37 = min([i for i in file if i % 37 == 0])
# max_73 = max([i for i in file if i % 73 == 0])

# for i in range(len(file) - 1):
#     a = file[i]
#     b = file[i+1]
    


# for i in range(len(file) - 2):
#     a = str(file[i])[::-1]
#     b = str(file[i + 1])[::-1]
#     c = str(file[i + 2])[::-1]


#     a_nechet = sum([int(a[i])])

# file_52 = [i for i in file if i % 100 = 52]


# file = open('/home/student/Загрузки/17-342.txt')
# file = [int(i) for i in file]
# for i in range(len(file) - 1):

#     if ((file[i] % 3 == 0) or (file[i + 1] % 3 == 0)):
#         lst.append(file[i] + file[i + 1])

# print(len(lst), max(lst))

# and ((file[i] - file[i + 1]) % 2 == 0)
#     for j in range(i+1, len(file)):
#         for k in range(i)
#         a = file [i]
#         b = file [j]
#         if ((a+b) % 9 == 0) :
#             lst.append(a + b)

# from itertools import product


# from itertools import product


# for x, y, w, z, in product([0,1], repeat = 4):
#     if ((x <= y) and (y == (not z)) and (z or w)) == 1:
#         print(y,w,z,x)


# F(5)= 14 + 3*8
# F(4) = 8 + 6
# F(3) = 8



# f = open('17.txt')
# a = [int(i) for i in f]
# s = 0
# mx = 0
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] % 160 != a[j] % 160) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
#             s += 1
#             mx = max(mx, a[i] + a[j])
# print(s, mx)


# def f(x,y):
#     if x > y : return 0
#     if x == 15: return 0
#     if x == y: return 1
#     return f(x+1,y) + f(x+2,y)
# print (f(3, 9) * f(9, 20))

# file = open('/home/student/Загрузки/24_demo.txt').read()

# cnt,max_cnt = 1,0
# for i in range(len(file)-1):
#     if file[i] != file[i+1]:
#         cnt += 1
#     else:
#         max_cnt = max(cnt,max_cnt)
#         cnt = 1

# print(max_cnt)

# print(bin(1500)[2:])
# print(int('11', base = 2))

# print(sorted('яйфцычвсумкапиертноьгшблщюдзжхэъ'))


# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2: 
#         return (F(n-1) - F(n-2)) * n
# print(F(8))

# from itertools import permutations

# lst = []
# for i in permutations('COMPUTER'):
#     s = ''.join(i)

#     if (s[-2] == 'E') and (s[:4] == "".join((sorted(s[:4])))):
#         lst.append(s)
# print(len(set(lst)))

# from fnmatch import fnmatch

# for i in range (161, 17*10**6, 161):
#     if fnmatch(str(i), '*1?*?68*'):
#         print(i)


# for i in range(206, 10**8+1, 206):
#     i = str(i)
#     if (i[:3] == '123') and (int (i[-4]) % 2 != 0):
#         if (int(i[-3]) % 2 == 0) and (i[-2:] == '56'):
#             i = int(i)
#             print(i,i//206)

# from fnmatch import fnmatch

# file = open(r'/home/student/Загрузки/24-228.txt').read().split('XX')

# lst = [int(i) for i in file if i.isdigit() and fnmatch(i, '3????78??45')]

# p=1
# max_ = str(max(lst))
# for i in max_:
#     i = int(i)
#     if i % 2 == 0:
        
#         p *= i
# print(p)

# for i in range (4023, 10**7 , 4023):
#     s = str(i)
#     if len(s) == 7:
#        if s [0] == '1' and int(s[1]) % 2 == 0 and int (s[2]) % 2 != 0:
#           if int(s[3]) % 2 == 0 and int(s[4]) % 2 != 0:
#               if int(s[5]) % 2 == 0 and int(s[6]) % 2 != 0:
#                   print(i , i// 4023)



# file = open(r'/home/student/Загрузки/24-224.txt').read()

# file = file.replace('BAC', '***')
# file = file.replace('CAB', '***')


# cnt, max_cnt = 0, 0

# for i in file:
#     if i == '*' :
#         cnt += 1
#         max_cnt = max (cnt,max_cnt)
#     else:
#         max_cnt = max (cnt, max_cnt)
#         cnt = 0

# print(max_cnt)




# def alg( n ):	 
#    s = f"{n:b}" 
#    if n % 2 == 0:	 
#      s = '1' + s + '10' 
#    else: 
#      s = '11' + s + '0' 
#    return int(s, 2) 
  
# count = 0 
# res = set() 
# for n in range(1000): 
#    if 800 <= alg(n) <= 1500: 
#      count += 1 
#      res.add( alg(n) ) 
  
# print( count ) 
# print( len(res) )

# from itertools import product

# cnt = 0
# for i in product(sorted( [ 'M', 'A', 'Н', 'Г', 'У', 'C', 'T',] ), repeat=6):
#     cnt += 1
#     s = ''.join(i)

#     if s[0]  ==  'О': 
#       print(s, cnt)
#       break

# print((7**4)*6)

# from itertools import product

# for A in range(200):
#     flag = True
#     for x,y in product(range(200), repeat= 2):
#         if ((2*x + 3*x > 30) or (x+y <= A))== 0:
#             flag = False
#     if flag:
#         print(A)
#         break

# f = open('/home/student/Документы/24-279.txt').read()
# alph = '0123456789ABCDEF'
# lst = []
# cnt = 0
# for i in f:
#     if i in alph:
#         cnt+=1
#     else:
#         lst.append(cnt)
#         cnt = 0


# print(max(lst))

# f = open('/home/student/Документы/24-278.txt').read()
# alph ='NKLF'
# alph2 = '02468'
# s=''
# lst = []
# for i in f:
#     if i in alph or i in alph2:
#         s+=i
#     else:
#         l = []
#         flag = False 
#         for j in range (0, 10, 2):
#             j =str(j)
#             if s.count(j) > 1: 
#                 flag = True
#                 l.append(j)
#         if flag: 
#             max_num = 0
#             for idx in l:
#                 max_num = max(max_num, s.rindex(idx) - s.index(idx))
#             lst.append(max_num)
#         s = ''
# print(max(lst)) 

# def is_prime(num):

#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# from fnmatch import fnmatch
# for i in range(2627, 10**9, 2627):
#     if fnmatch(str(i), '7*53?3*1'):
#         if is_prime (sum(list(map(int, str(i))))):
#             print(i, i//2627)


# from fnmatch import fnmatch

# def find_del(num):
#     lst=[]
#     for i in range(1, int(num**0.5)+1):
#         if num % i == 0:
#             lst.extend(i, num//i)
#     lst = sorted(set(lst))
#     return [i for i in lst if i % 2 == 0]
# cnt=0
# for i in range (6500, 10**10):
#     if fnmatch(str(i), '6*97*5?'):
#         a = find_del(i)
#         if len(d) >= 4:
#             print(i, sum(a))
#             cnt+=1
#     if cnt == 7: break

# from fnmatch import fnmatch

# lst =[]

# for i in range(2023, 10**10, 2023):
#     if fnmatch(str(i), '1*1'):
#         lst.append((sum(map(int, str(i))), i, i//2023))
# print(sorted(lst,reverse=True)[:2])

def factor(num):
    i = 2
    primefactor = []
    while i * i <= num:
        if num%i==0:
            primefactor.append(i)
            num //=1
        else:
            i+=1
    if num > 1:
        primefactor.append(num)
        return sorted(primefactor)