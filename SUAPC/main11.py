a=[]
c=[]
for k in range(1,11):
    b=int(input())
    a.append(b)
for i in range(1,11):
    # i=int(i)
    d=a[i-1]%42
    c.append(d)

print(len(set(c)))

# 왜 range 벗어난 오류가 생김??