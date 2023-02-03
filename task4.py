n = int(input("Введите число "))
zahla = 1
zahlb = 1
print("Fib(1) = 1")
print("Fib(2) = 1")
for i in range(3, n):
    temp = zahla + zahlb
    print("Fib(%d)" %i , + temp)
    zahla = zahlb
    zahlb = temp