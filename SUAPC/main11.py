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

# 왜 range 벗어난 오류가 생김?
# 리스트 슬라이싱은 0번부터 시작이어서
# 대괄호로 슬라이싱 
