cache = {}

def fib(n):
    global cache
    if n < 2:
        cache[n] = n
        return n
    elif cache[n]:
        return cache[n]
    else:
        temp = fib(n-1) + fib(n-2)
        cache[n] = temp
        return temp



if __name__ == '__main__':
    n = int(input("How much Fibonacci series you want? "))
    fibonacci = []
    for i in range(n):
        fibonacci.append(fib((i)))

    print(fibonacci)
