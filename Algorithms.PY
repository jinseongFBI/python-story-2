
#print(str(list(range(1,10001))).count('8'))

"""count=0
for i in range(10001):
  if '8' in str(i):
    count += str(i),count('8')


print(count)"""

#print(str(list(range(1,10001))).count('8'))

#str([i for i in range(10001)]).count('8')
"""s=[1,3,4,8,13,17,20]
m=max(s)
index=0
for i in range(len(s)-1):
  if m>s[i+1]-s[i]:
    index=1
    m=s[i+1]-s[i]

print(s[index], s[index+1])
"""
"""
print(bin(9),"\n" ,bin(30))

arr1=[3,20,28,18,11]
arr2=[5,1,21,17,28]
n=5

for i,j in zip(arr1,arr2):
  print(bin(i|j)[2:].zfill(n).replace('1','#').replace('0',' '))

"""
#print(bin(9|30)[2:].replace('1','#').replace('0',' '))
#for i,j in zip(arr1,arr2):
 # print(bin(i|j)[2:].zfill(n).replace('1', '#').replace('0', ' '))

"""def solution(n,arr1,arr2):
  answer=[]
  for i, j in zip(arr1,arr2):
    answer.append(bin(i|j)[2:].zfill(n).replace('1','#').replace('0',' '))
  return answer"""



"""
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수이쓴ㄴ 점수는 0점에서 10점까지이다.
점수와 함께 single(s),double(d),triple(t)영역이 존재하고 각영역 당첨시
점수에서 1제곱,2제곱,3제곱(점수^1,점수^2,점수^3)으로 계산한다. 
옵션으로 스타상(*),아차상(#)이 존재하며 스타상(*)당첨시 해당점수와 바로 전애ㅔ 얻은 점수를 각 2배로 만든다.
아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫번째 기회에서도 나올 수 있다. 이경우 첫번쨰 스타상(* )의 점수만 2배가 된다.
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이경우중첩된 스타상
"""
"""def solution(dartResult):
  answer=[]
  for num,i in enumerate(dartResult,1) :
    if i=="S":
      answer[-1] **=1 
    elif i=="D":
      answer[-1] **=2 
    elif i=="T":
      answer[-1] **=3 
    elif i=="*":
      answer[-1] *=2
      if len(answer)==2:
        answer[-2]*=2

    elif i=="#":
      answer[-1] *= -1
    else:
      if dartResult[num-1:num+1] == '10':
        answer.append(10)
      elif dartResult[num-2:num] != '10':
        answer.append(int(i))
  return answer

print(solution('1S3D*3T'))"""

"""
고객의 약간 동의를 얻어서 수집된 1~n 번으로 분류되는 개인정보 ㅇn개가 있습니다.
약관 종류는 여러가지 있으며 각 약관마다 개인정보 보관유효 기간이 정해져 있습니다. 당신은 각개인정보가 어떤약관으로 수집돼쓴ㄴ지를 알고 있습니다. ㅇ수집된 개인정보는 유효기간 전까지만 보관이 가능하며,유효기간이 지났다면 반드시 파기해야 합니다.
예를 들어 a라는 약관의 유효기간이 12 달이고 
2021년 1월 5일 수집된 개인정보가 a약관으로 수집되었다면 해당 개인정보는 ㅇ2022년 1월 4일까지 보관 가능하면 2022년 1월 5일 부터 파기해얄 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니ㅏㄷ.
모든 달은 28일 까지 있다고 가정합니다.
def solution(today, terms, privacies):

    for i in range (1,13):
     year[i]=int(privacies[0:4])
     month[i]=int(privacies[5:7])
     day[i]=int(privacies[8:10])

    for i in range(1,13):
        if terms[-1]==i:
            if day[i]==1:
                month[i]+=i
            if month[i]>12:
                month[i]-=12
                year[i]+=1
            day[i]==28
            break;

            month[i]+=i
            if month[i]>12:
                month[i]-=12
                year[i]+=1
            day[i]-=1
            break;

    answer = []


    y=int(today[0:4])
    m=int(today[5:7])
    d=int(today[8:])
    for i in range(1,13):
       if y>year[i] and m>month[i] and  d>day[i]:
        answer.append(i)
    
    return answer
"""