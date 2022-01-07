# 일반함수 와 비교
# 함수는 객체가 생성되었고 리소스, 즉 메모리가 할당됨
def mul_10(num : int) -> int:

    return num * 10

var_func = mul_10

print(var_func)
print(type(var_func))
print(var_func(5))

#람다식 변환
# 데이터 전처리나 간단한 함수등은 람다식으로 구현하는 것이 좋다

lambda_mul_10 = lambda num: num * 10

print('lambda',lambda_mul_10(8))

#함수도 파라미터로 받음
def lambda_in_func(x,y,func):
    return x,y,func(x)

print(lambda_in_func(7,10,lambda_mul_10))


print(lambda_in_func(15,10,lambda x:x**2))