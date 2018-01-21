def isPalindrome(n):
  n = str(n)
  for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i]:
      return False
  return True

#this is kinda brute force, but it works cuz numbers are pretty small
def solution():
  max_p = 0
  for i in range(999,99,-1):
    for j in range(999,99,-1):
      if isPalindrome(i*j):
        if i*j > max_p:
          max_p = i*j
  return max_p
        
print(solution())

#ANSWER = 906609
