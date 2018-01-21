"""
Since zeros don't matter in the overall sum, we can improve speed of the 
solution by getting rid of trailing zeros in the factorial. This just means
counting the number of fives that occur in each number.
"""

#count number of fives divisible in a given number
def countFive(n):
  count = 0 
  while(n % 5 == 0):
    n = n//5
    count += 1
  return count

#factorial function with countFive function included
def factorial(n):
  if n == 1:
    return 1
  return n*factorial(n-1)//(10**countFive(n))

#Putting each digit of the factorial into a list s
s = str(factorial(100))
s = list(s)
s = list(map(int,s))


#Printing sum of digits in list
print(sum(s))

#ANSWER:648
