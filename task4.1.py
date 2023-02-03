n = int(input("Please enter the sequence number of the Fibonacci number "))
numbera = 1
numberb = 1

for i in range(n):
    temp = numbera + numberb
    numbera = numberb
    numberb = temp

print('Fib(%d) = ' %n, + temp)
