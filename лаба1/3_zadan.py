import random
y=0
s=[]
for i in range(5):
    a=random.randint(1,10)
    if a==3:
        y=1
    s=s+[a]
if y==1:
    a=random.randint(1,10)
    s=s+[a]
else:
    a=3
    s=s+[a]
print (s)
 
