import time
import os
import psutil

n = 2  
os.makedirs("./primes", exist_ok=True)


startTime = time.time()
cpu_total = 0
cpu_count = 0


primeList = []

while n < 10000:
    is_prime = True  


    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:  
            is_prime = False
            break

    
    if(is_prime):
         primeList.append(n)

    
    cpuUtil = psutil.cpu_percent(interval=None)

    if(cpuUtil != 0.0):
        cpu_total += cpuUtil
        cpu_count += 1

    n += 1


endTime = time.time()
executionTime = endTime - startTime  
print(f"알고리즘 실행 시간: {executionTime} 초")

ioStart = time.time()

for p in primeList:
    file_path = "./primes/" + str(n) + ".txt"

    with open(file_path, "w") as file:
        file.write(str(p))


for filename in os.listdir("./primes"):
    file_path = os.path.join("./primes", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

ioEnd = time.time()


print(f"IO 시간: {ioEnd - ioStart} 초")
