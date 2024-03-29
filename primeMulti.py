import time
import os
import psutil
from concurrent.futures import ThreadPoolExecutor


def is_prime(n):
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    return True

def process_number(n):
    if is_prime(n):
        return n

startTime = time.time()


primeList = []

# 병렬 처리를 위한 스레드 풀 생성
with ThreadPoolExecutor() as executor:
    # 2부터 9999까지 소수 판별 작업을 병렬로 실행
    results = executor.map(process_number, range(2, 1000000))
    for result in results:
        if result is not None:
            primeList.append(result)

endTime = time.time()
executionTime = endTime - startTime
print(f"알고리즘 실행 시간: {executionTime} 초")

ioStart = time.time()

for p in primeList:
    file_path = f"./primes/{p}.txt"
    with open(file_path, "w") as file:
        file.write(str(p))


for filename in os.listdir("./primes"):
    file_path = os.path.join("./primes", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

ioEnd = time.time()
print(f"IO 시간: {ioEnd - ioStart} 초")
