n = int(input("Please enter the number "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fib(%d) = " %n, +fibonacci(n))