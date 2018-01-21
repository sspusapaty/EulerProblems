#function adds all the multiples of a number n that are less than a certain limit
def sumMult(n,limit):
  limit = (limit-1)//n
  return (n*limit*(limit+1))//2
  
#We care about multiples of 3 and 5 but since we can't count them twice, we subtract the intersection (15)
print(sumMult(3,1000) + sumMult(5,1000) - sumMult(15,1000))

#ANSWER = 233168
