f=open('17.txt','r')
f=[int(i.strip()) for i in f]
summ=0
cnt=0
m=0
for i in f:
    if i%2==0:
        summ+=i
        cnt+=1
srar=summ/cnt
cnt=0
for i in range(len(f)-1):
    if (f[i]%3==0 and f[i+1]<srar and f[i+1]%3!=0) or (f[i+1]%3==0 and f[i]<srar and f[i]%3!=0):
        m=max(f[i]+f[i+1],m)
        cnt+=1
print(cnt,m)