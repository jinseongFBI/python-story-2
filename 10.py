"""def adder(n1,n2):
  result=n1+n2
  return result

print(adder(1,2))


for i in (1,3,5,7,9):
  print(i,end=" ")

print("\n")

def who_are_you(name,age):
  print("이름:",name)
  print("나이:",age)

print(
who_are_you(name="윤성우",age=24),
who_are_you(age=24,name="윤성우")
)
print("\n")

print(1,2,3,end='m^^m')
print("\n")
print(1,2,3,sep=', ')
print(1, 2, 3, sep = ' _ ',end = ' m^^m')

print("\n")
"""

"""def who_are_you(name,age=0):
  print("이름: ",name)
  print("나이:",age)

print(who_are_you("홍길동"))"""

def func(s):
  s[0]=0
  s[-1]=0 

st=[1,2,3]
print(func(st))
# 변수:이름표 갖다 붙이기ㅣ
# s=1,2,3 st=1,2,3
# 본질에 더 가깝다

