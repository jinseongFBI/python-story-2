"""st=[1,2,3,4,5]
print(len(st),max(st),min(st),end="  ")

st.remove(4)
#st에 담겨져 있는 객체의 remove라는 함수를 호출 해서
#4라는 변수를 전달해라

print(st)"""

"""st=[1,2,3]
st.append(4) #하나씩
st.extend([5,6]) # 통째로
print(st)

st=[1,2,4]
st.insert(2,3)
print(st)

st.clear()
print(st)
"""
"""st=[]
for i in range(1,9):
  st.append(i)

print(st)
st.pop(0)

print(st)
print(st.count(1),st.index(2))
"""
"""str="  YoonSunWoo  "
print(str.count("o"))
print(str.count("oo"))

cp1=str.lstrip()
cp2=str.rstrip()
print(cp1)
print(cp2)
str="  Yoon_Sun_Woo  "
cp3=str.strip()
print(cp3)
rps=str.replace("oo", "ee",1)
print(rps)


ret=str.split('_')
print(ret)

str="what is important is \n that you should choose what is best for you"

print(str.find("is"))
print(str.rfind("is"))

print(str)"""
# "",'',구분하는 이유는 ''를 쓸수도있고 ""를 쓸수도있어서
#혼동되니깐 아니면 이스케이프 문자 써도되고 \' \" 문자열을 구성하는 과정 "
"""
st=[1,2,3,4,5]
st.clear()
print(st)

st=[1,2,3,4,5]
st[:]=[]
print(st)

st=[1,2,3,4,5]
st[2:]=[]
print(st)

st=[1,2,3,4,5]
del st[:]
print(st)

st=[1,2,3,4,5]
del st[3:]
del st[0]
print(st)"""