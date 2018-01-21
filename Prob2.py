#Adds fibonacci numbers to a hash table as they are generated. Keeps a sum of even numbers too

def fibDic(n):
  dic = {1:1,2:2}
  sum = 0
  i = 2
  while dic[i] < n:
    if dic[i] % 2 == 0:
      sum += dic[i]
    i += 1
    if i not in dic:
      dic[i] = dic[i-1] + dic[i-2]
  return sum
  
print(fibDic(4000000))

#ANSWER = 4613732
