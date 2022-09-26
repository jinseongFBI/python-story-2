"""def main():
  sum=0
  for i in range(0,11):
    sum+=i
  
  print(sum)

def add():
  n=0
  while n<3:
    print(n,end=" ")
    n+=1




add()
print(end="\n")
main()
"""

"""
for<변수> in <반복범위>:
  <for에 속하는 문장들>

while <반복조건>:
  <조건이 True인 경우 반복 실행할 문장들>
"""

"""def main():
  i=1
  sum=0
  while i<11:
    sum=sum+1
    i=i+1
    print("sum= ",sum,end="\n ")
  
  print(i)"""

"""def main():
    i=1
    sum=0
    while sum<=100:
      sum=sum+i
      i=i+1
    print(i-1,"더했을때의 합",sum,end='')
"""

"""def main():
  i=0
  while True:
    print(i,end=" ")
    i=i+1
    if i==20:
      break
  
  print("\n 벗어난값",i)
main()"""
"""def main():
  i=1
  sum=0
  while True:
    sum=sum+i
    if sum>100:
      print(i,"더했을때의 합",sum,end=' ')
      break
    i=i+1

main()"""
"""for i in range(1,11):
  print(i,end=" ")

print("\n")

for i in range(0,11):
  if(i%2==0):
    continue
  print(i,end=" ")"""
# break 탈출 continue 생략 ㅑ


"""i=0
while i<10:
  i=i+1
  print(i,end="")

print("\n")

i=0
while i<10:
  i=i+1
  if i%3==0: continue
  print(i,end=' ')"""

for i in [1,2]:
  for j in ['a','b','c',10]:
    print(j*i,end=' ')

print("\n")

sr=['father','mother','brother']
cnt=0
for s in sr:
  for c in s:
    if c=='r':
      cnt=cnt+1

print(cnt)
