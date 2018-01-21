#Check if a number is prime by checking divisibility by every number less than the square root
def largePrimeFac(n):
  large = 0
  limit = int(n**0.5)
  for i in range(2,limit+1):
    if n%i == 0:
      n = n//i
      if i > large:
        large = i
  return large
  
print(largePrimeFac(600851475143))

#ANSWER = 6857
