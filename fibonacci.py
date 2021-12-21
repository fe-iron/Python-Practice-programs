def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    n = int(input("How much Fibonacci series you want? "))
    fibonacci = []
    for i in range(n):
        fibonacci.append(fib((i)))

    print(fibonacci)
