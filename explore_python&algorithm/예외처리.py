

"""
문법적으로 예외는 없어도, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요하다
"""

"""SyntaxError : 문법오류"""

# print('test)

# if True
#     pass

# x -> y

"""NameError : 참조변수없음"""

"""zerodivisionError : 0나누기 에러"""

"""IndexError : 인덱스범위에러"""

"""KeyError"""

dic = {"1": "one", "2": "two"}
# print(dic["3"]) 바로 접근하면 에러발생
print(dic.get("3")) #get으로 접근하면 None


"""AttributeError : 모듈, 클래스에 있는 잘못된 속성을 사용하면 발생"""

import time
print(time.time())
# print(time.month()) #없는 함수를 사용해서 에러발생

"""ValueError : 참조값이 없을 때 발생 """

test = [1,2,3,4,5]

# print(test.index(6))

"""FileNotFoundError"""

# with open("nonefile","r") as f:
#     f.read()


"""TypeError"""



""" 항상 예외가 발생하지 않을것으로 가정하고 먼저 코딩하자"""
""" 그 후 런타임 예외 발생시 예외처리 코딩을 권장한다 == EAFP 코딩 스타일 """

"""예외처리 기본"""

"""
try
except
else - 에러가 발생하지 않으면 실행된다.
finally - 항상실행된 
"""


name = ["one","two","three"]

try:
    z = "two"
    x = name.index(z)
    print("리스트안에 있다!")

except ValueError: #어떤에러가 발생할지 모를때는 안써줘도된다.
    print("리스트안에 없다!")

else:
    print("else!!")

print('*'*10)

try:
    z = "tw"
    x = name.index(z)
    print("리스트안에 있다!")

except ValueError: #어떤에러가 발생할지 모를때는 안써줘도된다.
    print("리스트안에 없다!")

else:
    print("else!!")

finally:
    print("finally ok!!")


"""어떤 프로그램에서 특정상황을 찾고싶을 대 expcept를 발생해준다"""