# 람다 표현식
def add (a,b):
    return a+b

print((lambda a,b: a+b)(3,7))

# 📌 리스트를 바꾸는 메서드
# list.sort(), list.reverse(), list.append(x), list.extend(iterable), list.remove(x), list.clear() …
# 리스트 자체를 제자리(in-place)에서 변경


# 📌 새 객체를 만들어서 돌려주는 함수
# sorted(iterable) → 정렬된 새 리스트 반환
# reversed(iterable) → 역순 반복자 반환 (원본 안 바꿈)
# copy.copy(obj) → 얕은 복사 반환

# 반환값이 있으니까 바로 print() 안에 넣어도 ok

# 3. 람다와 iterable 차이

# lambda a,b: a+b → 익명 함수 (함수 자체)
# l=[1,2,3] 같은 리스트 → iterable (반복 가능한 자료구조)
# 즉 map의 첫 번째 인자는 함수 (int, lambda, str.upper, …)
# 두 번째 이후 인자는 iterable (리스트, 튜플, 문자열, range 등)이 들어가야 해요.

# map(int, input().split()) 쓸 때의 int랑,
# map(lambda a,b: a+b, l, ll) 쓸 때의 lambda는 똑같이 함수