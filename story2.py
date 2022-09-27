"""r1=[1,2,3]
r2=[1,2,3]
#print(r1==r2,"\n",r1 is r2)

r2=r1
#print(r1 is r2)

r1=['John',('man','USA'),[175,23]]
r2=list(r1)
 
#print(r1 is r2)
#print(r1[0] is r2[0],r1[1] is r2[1],r1[2] is r2[2])

J2021=['John',('man','USA'),[175,23]]
J2022=list(J2021)
J2022[2][1]+=1
#print(J2021,J2022)

J2021=['John',('man','USA'),[175,23]]
import copy
J2022=copy.deepcopy(J2021)
J2022[2][1]+=1
print(J2021,J2022)
print(( J2021[0] is J2022[0] ) and(J2021[1] is J2022[1]))
print(J2021[2] is J2022[2])

d1=(1,2,3)
d2='Please'
c1=tuple(d1)
c2=str(d2)
print(d1 is c1)
print(d2 is c2) """

r1=[1,2,3]
r2=[]
r3=[1,2,[3,4]]
r4=list('Hello')
r5=list((5,6,7))
r6=list((range(0,5)))

r1=[1,2,3,4,5]
r2=[]
for i in r1:
  r2.append(i*2)

#print(r2)

r1=[1,2,3,4,5]
r2=[x**2 for x in r1]
#print(r2)

r1=[1,2,3,4,5]
r2=[x+10 for x in r1]
r3=[x**2+10 for x in r1]
#print(r3)

r1=[1,2,3,4,5]
r2=[]
for i in r1:
  if i%2:
    r2.append(i*2)

print(r2)

r1=[1,2,3,4,5]
r2=[x*2 for x in r1 if x % 2]
print(r2)

r1=['Black',"white"]
r2=['Red','Blue','Green']
r3=['0','1','2']
r4=[]
for t in r1:
  for p in r2:
    for j in r3:
      r4.append(t+p+j)

#print(r4)

#r4=[t+p+j for t in r1 for p in r2 for j in r3]
#print(r4)

r=[n*m for n in range(2,10) for m in range(1,10)]
#print(r)

r=[n*m for n in range(2,10) for m in range(1,10) if(n*m)%2]
print(r)
