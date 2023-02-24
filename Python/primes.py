import time
start = time.time()
print("Started in Python")
i = 1
primes = 0
while i < 150000:
    i += 1
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primes += 1
end = time.time()
executionTime = end - start
print("Execution time: " + str(executionTime))
print("Primes found: " + str(primes))
print("Primes per second: " + str(primes / executionTime))

input("Press something to exit...")
