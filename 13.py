#클래스와 객체
#가볍다,간결하다,
#저역변수와 지역변수 
#지역변수는 임시적인
"""
def func(n):
  lv=n+1
  print(lv)

func(12)

cnt=100
cnt+=1
def func():
  print(cnt)

func()"""
"""
cnt=100
def func():
  cnt=0
  print(cnt)

func()
print(cnt)"""

"""cnt =100
def func():
  global cnt
  cnt=0
  print(cnt)

func(
)
print(cnt)
"""
#객체지향 프로그래밍(Object Oriented Programming)
"""
C++,java,C# 
좋은코드 
데이터 접근은 함수를 통해서 
"""
#family_age1.py
"""fa_age=39
def up_fa_age():
  global fa_age
  fa_age+=1
def get_fa_age():
  return fa_age

def main():
  print("2019년...")
  print("아빠:",get_fa_age())
  print("2020년..")
  up_fa_age() # 아빠나이 1살증가
  print("아빠:",get_fa_age())

main()"""
#클래스=틀 /객체 =찍어내자
#자동차 설계도=클래스
#설계도 기반으로 만들어진 실제 자동차=객체

#에어컨 설계도<클래스>
#설계도 기반으로 만들어진 실제 에어컨<객체>

class AgeInfo:
  def up_age(self):
    self.age+=1
  def down_age(self):
    self.age-=1
  def get_age(self):
    return self.age
""" 
def main():""
  fa=AgeInfo()
  fa.age=39
  print("현재 아빠 나이...")
  print("아빠:",fa.get_age())
  print("1년전 ...")
  fa.down_age()
  print("아빠:",fa.get_age())""

main()

인스턴스(안에있는) 변수: 인스턴스(객체)안제 존재하는 변수
인스턴스(안에있는)메소드:인스턴스(객체)안에 존재하는 메서드
"""
"""def main():
  fa=AgeInfo()
  mo=AgeInfo()
  so=AgeInfo()
  fa.age=62
  mo.age=57
  so.age=28
  print("현재 나이는?",
  fa.get_age(),mo.get_age(),so.get_age())

  fa.up_age()
  mo.up_age()
  so.up_age()
  print("2023년  나이는?",
  fa.get_age(),mo.get_age(),so.get_age())

main()"""

"""class AgeInfo:
  def up_age(self):
    self.age+=1
  def get_age(self):
    return self.age
  def set_age(self,age):
    self.age=age

def main():
  fa=AgeInfo()
  fa.set_age(39)
  fa.up_age()
  print("1년후 아빠나이:",fa.get_age())

main()"""

# self 너 뭐냐 ? 
# 메소드{ 1매개변수 self
#         self
#age->self 간다.

#생성자(초기화 메소드)
"""10.py
java,c++ constructor <생성자>

파이썬 Initializer <생성자= 본질은 동일>
Generator<생성자 절대x=제너레이터 
"""
"""class Const:
  def __init__(self):
    print("new!")
  
def main():
    o1=Const()
    o2=Const()
# 객체 1당 생성자 1나 
# 객체 생성 초기화 를 한번에 하는법
#생성자

main()"""
class Const:
  def __init__(self,n1,n2):
    self.n1=n1
    self.n2=n2
  def show_data(self):
    print(self.n1,self.n2)

def main():
  o1=Const(1,2)
  o2=Const(3,4)
  o1.show_data()
  o2.show_data()

main()
#파이썬의 모든 값은 객체
n=1000
n.bit_length()
f=3.14
f.is_integer()
