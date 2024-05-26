
file = open('/home/student/Загрузки/9.csv')
cnt = 0

for string in file:
    lst = list(map(int, string.split(';')))
    uniq = set(lst)

    if len(uniq) == 5:
        sum_repeat = sum(lst) - sum(uniq)
        if ( sum(uniq)//len(uniq) <= sum_repeat*2 ):
            cnt += 1
print(cnt)