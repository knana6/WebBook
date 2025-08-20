a=list(map(int,input().split()))
# map int input() split() 이거 기본 암기
# map ㅇ은 이터레이터 형태, list 변환 필요
if a[0]> a[1]:
    print(">")
elif a[0]==a[1]:
    print("==")
else:
    print("<")

# slicing - [ ] 