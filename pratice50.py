"""print("안녕하세요")"""
"""a=1
b=1
print(a+b)"""
"""_myname='samsjang'
my_name_='홍길동'
Myname2="Hong gil-dong"
counter=1
Counter=2
print(_myname, my_name_, Myname2,counter,Counter)"""
"""and=1
print(and)"""
"""import keyword
keyword.kwlist"""

"""#4
number1=1
pi=3.4
flag=True
char='x'
chars='I love Python'
print(number1, pi, flag, char, chars)

number=1
number=number+2
print(number)
number='one'
print(number)"""
#5
# 주석 처리 예시임 
# 만든 날짜:2022-07-21
# 삼중 따옴표로 특정영역 주석처리 예시 ㅇ
"""a=1
b=5
print(a+b)"""
#a=1
#b=5
#print(a+b)

#6
"""int_data=1
float_data=3.14
complex_data=1+5j
str_data1='I love Python'
str_data2="반갑습니다."
list_data=[1,2,3]
tuple_data=(1,2,3)
dict_data={0:'False',1:'True'}
print(type(int_data))
print(type(float_data))
print(type(complex_data))
print(type(str_data1))
print(type(str_data2))
print(type(list_data))
print(type(tuple_data))
print(type(dict_data))"""

#7
"""a=200
msg='i love Python'
list_data=['a','b','c']
dict_data={'a':97,'b':98}
print(a, msg, list_data, dict_data['a'], dict_data)"""

#8
"""listdata=['a','b','c']
if 'a' in listdata:
  print('a가 listdata에 있습니다.')
  print(listdata)
else:
  print('a가 listdata에 존재하지 않습니다.')"""

#9
"""x=1
y=2
if x>=y:
  print('x가 y보다 크거나 같습니다.')
else:
  print('x가 y보다 작습니다.')"""

#10
"""x=2
y=1
if x>y:
  print('x가 y보다 큽니다.')
elif x<y:
  print('x가 y보다 작습니다.')
else:
  print('x와y 가 똑같습니다.')"""
"""
#11
scope=[1,2,3,4,5]
for x in scope:
  print(x)

print('')
str = 'abcdef'
for c in str:
  print(c)

print('')

list=[1,2,3,4,5]
for c in list:
  print(c)

print('\n')

ascii_codes={'a':97,'b':98,'c':99}
for c in ascii_codes:
  print(c) 

print('\n')

for c in range(10):
  print(c)"""

#12
"""scope=[1,2,3,4,5]
for x in scope:
  #print(x)
  if x<3:
   # print(x)
    continue
   # print(x)
  else:
    #print(x)
    break
    #print(x)
print(x)"""

"""scope=[1,2,3,4,5]
for x in scope:
  print(x)
  if x>=3:
    break"""

#13
"""
scope=[1,2,3]
for x in scope:
  print(x)
  if x==3: break
else:
  print('Perfect')"""

#14

"""x=0
while x<10:
  x=x+1
  if x<3:
    continue
  print(x)
  if x>7:
    break"""

"""x=1
total=0
while 1:
  total=total +x
  if total>100000:
    print(x)
    print(total)
    break
  x=x+1"""

#15
"""val=None
condition=1
if condition==1:
  val=[1,2,3]
  print(val)
else:
  val='I love Python'
  print(val)"""

#16
"""int_data=10
bin_data=0b10
oct_data=0o10
hex_data=0x10
long_data=1234567890123456789
print(int_data, bin_data, oct_data, hex_data, long_data)"""

#17
"""f1=1.0
f2=3.14
f3=1.56e3
f4=-0.7e-4
print(f1, f2, f3, f4)"""
#18
"""c1=1+7j
print(c1.real);print(c1.imag)
c2=complex(2,3)
print(c2, c2.real, c2.imag)"""

#19
"""a=1 
b=2 
ret=a+b
print('a와 b를 더한 값은',end="")
print(ret, end="")
print('입니다.')"""
#20
"""from re import A
"""
"""
a=2 
b=4
ret1=a+b
ret2=a-b
ret3=a*b
ret4=a/b
ret5=a**b
ret6=a+a*b/a
ret7=(a+b)*(a-b)
ret8=a*b**a
list1=[ret1,ret2,ret3,ret4,ret5,ret6,ret7,ret8]
x=0
for x in range(0,8):
  print(list1[x])"""

#21 
"""a=0
a+=1
a-=5
a*=2
a/=4"""

#22
"""a=True
b=False
print(a==1)
print(b!=0)"""

#23
"""x=1 
y=2
str1='abc'
str2='python'
print(x==y)
print(x!=y)
print(str1==str2)
print(str2=='python')
print(str1<str2)"""

#24
"""bool1=True;bool2=False;bool3=True;bool4=False
print(bool1 and bool2)
print(bool1 and bool3)
print(bool2 or bool3)
print(bool2 or bool4)
print(not bool1)
print(not bool2)"""

#25
"""bit1 =0x61
bit2=0x62
print(hex(bit1&bit2))
print(hex(bit1|bit2))
print(hex(bit1^bit2))
print(hex(bit1>>1))
print(hex(bit1<<2))"""

#26 
"""strdata='abcde'
listdata=[1,[2,3],'안녕']
tupledata=(100,200,300)
print(listdata, tupledata )"""

#27 
"""strdata="Time is money"
listdata=[1,2,[1,2,3]]
print(strdata[5])
print(strdata[-2])
print(listdata[0])
print(listdata[-1])
print(listdata[2][-1])"""

#28
"""strdata="Time is money"
print(strdata[1:5])
print(strdata[:7])
print(strdata[9:])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])
print(strdata[::2])"""

#29
"""strdata1 ='I love'; strdata2='Python' ; strdata3='you'
listdata1=[1,2,3]; listdata2=[4,5,6]
print(strdata1 +" "+ strdata2)
print(strdata1 +" "+ strdata3)
print(listdata1 + listdata2)"""

#30
"""artist="BTS!"
fan='ARMY'
dispdata=fan+'들이외칩니다.'+artist*3
print(dispdata)"""

##31
"""strdata1="I love python"
strdata2="나는 파이썬을 사랑합니다."
listdata=['a','b','c',strdata1,strdata2]
print(len(strdata1))
print(len(strdata2))
print(len(listdata))
print(len(listdata[3]))"""

#32
"""listdata=[1,2,3,4]
ret1=5 in listdata
ret2=4 in listdata
print(ret1)
print(ret2)
strdata='abcde'
ret3='c' in strdata
ret4='f' in strdata
print (ret3, ret4)"""

#33
#strdata1='나는 파이선 프로그래머이다.'
#strdata2="You are a programmer"
#strdata3="""I love python. you love python too!"""
#strdata4="My son's name is John"
#strdata5='문자열 "abc" 길이는 3입니다.'
##print(strdata1)
#print(strdata2)
#print(strdata3)
#print(strdata4)
#print(strdata)
 
#34
"""txt1='자바'
txt2='파이썬'
num1=5
num2=10
print('나는 %s보다 %s에 더 익숙합니다'%(txt1,txt2))
print('%s은 %s보다 %d배 더 쉽습니다.'%(txt1,txt2,num1))
print('%d+ %d=%d'%(num1,num2,num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d %% 포인트 증가했다.'%(num1))"""

"""from time import sleep
for i in range(100):
  msg='\r진행률%d%%'%(i+1)
  print(''*len(msg),end='')
  print(msg,end="")
  sleep(0.1)"""