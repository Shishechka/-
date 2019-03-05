a=[str(i) for i in input('Введите значения через пробел ').split()]
s=[]
for i in range(len(a)):
    s=a[i]
    y=len(s)-1
    if s[y]=='r':
        print(a[i])

