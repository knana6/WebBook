a, b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b) #백준은 보통 정수 나눗셈 원함
print(a%b)

#map 함수는 데이터 변환하는 도구.
# 기본 형태: map(함수, 객체)
# 함수- int, str, float, lambda
# 객체- input, 리스트, 문자열, 튜플 등

# 가장 많이 보이는 형태
# a,b= map( int, input().split()) 