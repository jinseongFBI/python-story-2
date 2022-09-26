# 모듈의 이해 그리고 수학 모듈이용하기
# 만들기 가져다 쓰기 

# circle.property
"""
circle.py
PI=3.14

def ar_circle(rad):
  return rad * rad * PI

def ci_circle(rad):
  return rad *2 *PI
"""
"""import circle

def main():
  r=float(input("반지름 입력:"))
  ar=circle.ar_circle(r)
  print("넚이",ar)
  ci=circle.ci_circle(r)
  print("둘레",ci)


main()
"""
"""from circle import ar_circle
from circle import ci_circle
# from circle import ar_circle,ci_circle


def main():
  r=float(input("반지름입럭:"))
  ar=ar_circle(r)
  print("넓이:",ar)
  ci=ci_circle(r)
  print("둘레:",ci)

main()"""

#함수의 이름이 충돌이 났을때 방지
#또는 as로 모듈의 이름 줄이기 
"""from circle import ci_circle as cc
def ci_circle(rad):
  print("둘레:",rad*2*3.14)

def main():
  r=float(input("반지름입력:"))
  ci_circle(r)
  cc(r)

main()"""
#빌트인 함수
#import 선언 없이 그냥 언젠든 호출 가능한 함수
#빌트인 모듈
#위치 신경 쓰지 않고 언제든 import 할 수 있는 모듈

import math

print(math.fabs(-10))