"""print(True,False,end="\n")
print(3>10)
print(3<10)

r=3<10 
print(r)
print(type(True),
type(False))"""
"""num=10
if num>0:
  print("양의 정수입니다.")"""



"""def main():
  num=int(input("양의 정수를 입력:"))
  if num>0:
    print("양의 정수입니다.")
  elif num==0:
    print("ㅇ 입니다.")
  else:
    print("양의 정수가 아닙니다.")

main()"""

"""def main():
  num=int(input("숫자를 입력하세요:"))
  if num>0:
    print(num,"은 양의 정수 입니다.")
  elif num==0:
    print(num,"은 0 입니다.")
  elif num<0:
    print(num,"음수 입니다.")
  else:
    print(num,"숫자가 아닙니다.")

main()"""

"""#2의 배수이면서 3의 배수 입력
def main():
  num=int(input("2의 배수이면서 3의 배수 입력:"))
  if(num%2==0):
    if num%3==0:
      print("ok")
    else:
      print("no")
  else:
    print("no")

main()"""

"""def main():
  num=int(input("정수입력:"))
if num%2==0 and num%3==0:
  print("ok")
else:
  print("no")"""

"""print('abc'=='abc',
'abc'!="abc",end="\t")

[1,2,3]==[1,2]
[1,2,3]!=[1,2]

st1="123"
st2="OneTwoThreee"
print(st1.isdigit(),st2.isdigit())

print(end="\n")
str="I AM ironMan"
print(str.startswith("I"),str.endswith("Man")
)
"""
"""def main():
  pnum=input("전화번호를 입력하세요.")
  if pnum.isdigit and pnum.startswith("010"):
    print("정상적인 입력입니다.")
  else:
    print("정상적이지 않은 입력입니다.")

main()"""

"""s="Tomato<spaghetti"
if "ghe" in s:
  print("o")
else:
  print("x")

"""
print(
3 not in [1,2,3],
235 not in [234,233,222],
"he" not in "hello",
"oo" not in "hello",
end='__'
)

print(end="\n")

num=1
if num:
  print("num은 0이 아닙니다.")

