def test(x):

    y1 = x *10
    y2 = x *100
    y3 = x *1000

    return [y1,y2,y3]

y1,y2,y3 = test(100)
new = test(999)

print(type(new))
print(type(y3))
print(y2)

#함수 꿀팁

def args_func(*test1):
    print(test1)

args_func('hong')
args_func('hong','kang')
args_func('hong','lee','park')

def args_func_enumerate(*test1):
    for i,v in enumerate(test1):
        print(i,v)

args_func_enumerate('hong','lee','park')


#kwargs

def kwargs_func(**test2):
    print(test2)

kwargs_func(new1='hong',new3='lee',new2='park',new4='kang')

#혼합

def example(test1,test2,*test3,**test4):
    print(test1,test2,test3,test4)
example(10,2)
example(10,2,'hong','lee')
example(10,2,'hong','lee',new1='hong',new3='lee',new2='park')

#고급 프로그래밍으로 나가는 길 = 중첩함수(용어:클로저) =>데코레이터에 쓰임

def nested_func(num):
    def func_in_func(num):
        print('fucn in func',num)
    print("in func")
    func_in_func(num+10000)

nested_func(50000)


#힌트 (int 가 입력으로 들어와서 list가 나오는 구나 정도임.
# 에러나 예외처리는 아니지만 변수에 대한 안내역할임)

def test2(x : int) -> list:

    y1 = x *10
    y2 = x *100
    y3 = x *1000

    return [y1,y2,y3]

print(test(5))
print(test(5.0))


