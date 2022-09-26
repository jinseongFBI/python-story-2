# 튜플과 레인지

"""lst=[1,2,3]
print(lst)
print(type(lst))


tpl=(1,2,3)
print(tpl)
print(type(tpl))

frns=[['동수',131120],['진우',130312],
['선영',130904]
]
print(frns)"""

"""frns=[['동수',131120],
['진우',130312],['선영',130904]
]

for i in range(0,3):
  for j in range(0,2):
    print(frns[i][j])
"""
"""
nums=(3,2,5,7,1)
print(len(nums),max(nums),min(nums))
print("\n",nums.count(2),nums.index(1))"""
"""
nums=(1,2,3)
print(3 in nums,2 not in nums)
print(nums+(4,5),"\n",nums*2,"\n",nums[0:3])
"""
"""print(list((1,2,3)),
list(range(1,5)),
list("Hello"),"\n")

print(tuple([1,2,3]),
tuple(range(1,5)),
tuple("Hello"),"\n")"""

#lst=list(range(1,16))
#print(lst)

#tpl=tuple(range(1,16))
#print(tpl)
"""
print(
range(1,10,2),"\n",
range(1,10,3),"\n",

list(range(1,10,2)),"\n",
list(range(1,10,3)),"\n")

"""
print(
list(range(2,10)),"\n",
list(range(2,10,1)),"\n",
list(range(10,2)),"\n",
list(range(10,2,1)),"\n",
list(range(10,2,-1)),"\n",
list(range(10,2,-2)),"\n",
list(range(10,2,-3)),"\n",
)
