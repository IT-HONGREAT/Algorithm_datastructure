def fib_tab(n):

    fibo = [0,1,1]

    for i in range(3, n + 1):
        fibo.append(fibo[i-1]+fibo[i-2])

    return fibo[n]



print(fib_tab(10))
print(fib_tab(50))
print(fib_tab(100))