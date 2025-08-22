a=int(input())
# if a//100==0:
#     if a//400==0:
#         print("1")
#     else: 
#         print("0")
# else:
#     print("0")

# if a//4==0:
#     if a//100==0:
#         print("0")
#     elif a//400==0:
#         print("1")
#     else:
#         print("1")

# else:
#     print("0")

if a % 4==0:
    if a % 100!= 0 or a % 400== 0:
        print("1")
    else:
        print("0")
else:
    print("0")
    # 괄호 잘닫기

# //: 몫
# % : 나머지
