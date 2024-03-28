import time

startTime = time.time()

n = 2  

while n < 300000:
    is_prime = True  

    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:  
            is_prime = False
            break

    if is_prime:
        print(n)

    n += 1


endTime = time.time() 
executionTime = endTime - startTime  
print("실행 시간:", executionTime)