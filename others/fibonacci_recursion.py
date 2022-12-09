# Santiago Garcia Arango, December 2022

def fib(n):
    """
    Fibonacci sequence (Nth number) via recursion approach.
    Complexity: O(2^n)
    """
    if n == 1 or n ==2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


if __name__ == "__main__":
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(9))
    print(fib(10))
