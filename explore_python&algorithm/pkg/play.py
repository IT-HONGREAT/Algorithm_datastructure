from zerobase.pkg.fibo import Fibonacci

Fibonacci.fib(300)

print("2",Fibonacci.fib2(300))
print("2",Fibonacci().title)

#권장하지 않는 사용법
from zerobase.pkg.fibo import *
print("2",Fibonacci.fib2(10))


#또다른 사용법 = Alias

from zerobase.pkg.fibo import Fibonacci as fb
print("2",fb.fib2(20))

#함수형사용법

import zerobase.pkg.calc as c
print(c.mul(3,6))

