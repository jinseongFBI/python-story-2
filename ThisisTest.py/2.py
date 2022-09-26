"""
n=int(input())
data=list(map(int,input().split()))

data.sort(reverse=True)
print(data)"""
"""n, m, k =map(int, input().split)
print(n, m, k)"""
#import sys
#sys.stdin.readline().rstrip()
"""data=sys.stdin.readline().rstrip()
print(data)"""
n, m, k= map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

while True:
  for i in range(k):
    if m==0:
      break
    result+= first
    m=m-1 
  if m==0:
    break
  result=result+second
  m=m-1

print(result)