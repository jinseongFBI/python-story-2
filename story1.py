"""s='Garbage Collection'
print(s)

r=[1,2,3]
r='simple'

print(r)
r1= [1,2,3]
r2=r1

r1="simple"
r2="happy"

print("r1=",r1,"\n","r2=",r2)
"""
#--------------------------------------------------------
#immutable & mutable  
"""
r=[1,2]
print(id(r))

r+=[3,4]
print(r)

print(id(r))"""
"""t=(1,2)
print(id(t))

t+=(3,4)
print(id(t))"""
# 성격에 따라 달라지는 함수 정의
def add_last(m,n):
  m+=n

r=[1,2]
add_last(r,[3,4])
#print(r)

t=(1,3)
add_last(t, (5,7))
#print(t)

def add_tuple(t1,t2):
  t1+=t2
  return t1

tp=(1,3)
tp=add_tuple(tp,(5,7))
#print(tp)

def min_max(d):
  d.sort()
  print(d[0],d[-1],sep=', ')

l=[3,1,5,4]
min_max(l)
print(l)

print("------------------------")

def min_max2(d):
  d=list(d)
  d.sort()
  print(d[0],d[-1],sep=', ')

l=[3,1,5,4]
min_max2(l)
print(l)