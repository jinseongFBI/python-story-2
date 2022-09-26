# 예외 처리
# 예외 못하는 상황을 예외처리 한다.
# 1.처리가능 2.처리 불가능(코드 수정)
lst=[1,2,3]
#print(lst[3])

#3+"coffee"
#3/0

"""age=int(input("나이를 입력:"))
print(age)"""
"""
def main():
  print("안녕하세요")
  try:
    age=int(input("나이를 입력:"))
    print("입력하신 나이는 다음과 같습니다.",age)
  except ValueError:
    print("입력이 잘못되었습니다.")
  
  print("만나서 반가웠습니다.")

main()"""

"""def main():
  print("안녕하세요.")
  while True:
    try:
      age=int(input("나이를 입력하세요:"))
      print("입력하신 나이는 다음과 같습니다.",age)
      break
    except ValueError:
      print("입력이 잘못되었습니다.")
  print("만나서 반가웠습니다. ")


main()"""

def main():
  bread=10
  try:
    people=int(input("몇명?"))
    print("1인당 빵의수:",bread/people)
    print("맛있게 드세요")
  except ValueError as msg:
    print("입력이 잘못되었습니다.")
    print(msg)
  except ZeroDivisionError as msg:
    print("0으로 나눌 수 없습니다.")
    print(msg)
  finally:
    print("어쨋든 프로그램은 종료합니다.")
   # except ValueError:
  #  print("입력이 잘못되었습니다.")
 # except ZeroDivisionError:
 #   print("0으로는 나눌 수없습니다.")

main()
# try:~~
# except: 이렇게하면 모든 예외가 다걸림 