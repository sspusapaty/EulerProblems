primeList = [2]

def isPrime(n):
  for e in primeList:
    if n%e == 0:
      return False
  return True
  
count = 1
num = 3
while count < 10001:
  if isPrime(num):
    primeList.append(num)
    count += 1
  num += 2
print(primeList[-1])
