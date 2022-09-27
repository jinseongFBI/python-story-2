#137
"""f=open('stockcode.txt','r')
data=f.read()
print(data)
f.close()"""

#138

"""f=open("stockcode",'r')
line_num=1
line=f.readline()
while line:
  print('%d %s' %(line_num,line),end="")
  line=f.readline()
  line_num+=1
f.close()
"""
#139
"""f=open('stockcode','r')

lines=f.readlines()

for line_num,line in enumerate(lines):
  print('%d %s'%(line_num+1,line),end='')

f.close()"""

#140
"""text=input("파일에 저장할 내용을 입력하세요")
f=open('mydata.txt','w')
f.write(text)
f.close()
"""
#응용
"""f=open("mydata.txt",'r')
data=f.read()
print(data)
f.close()"""
#141

"""count=1
data=[]
print("파일에 내용을 저장하려면 내용을 입력하지 말고 [ENTER]를 누르세요.")
while True:
  text=input('[%d] 파일에 저장할 내용을 입력하세요: '%count)
  if text=='':
    break
  data.append(text+'\n')
  count+=1

f=open('mydata.txt','w')
f.writelines(data)
f.close()
"""

#142

"""f=open('stockcode','r')
h=open('stockcode_copy.txt','w')

data=f.read()
h.write(data)

f.close()
h.close()"""

#143
"""bufsize=1024
f=open('img_sample.jpg','rb')
h=open('img_sample_copy.jpg','wb')

data=f.read(bufsize)
while data:
  h.write(data)
  data=f.read(bufsize)

f.close()
h.close()"""

#144
"""
with open('stockcode','r') as f:
  for line_num,line in enumerate(f.readlines()):
    print('%d %s'%(line_num+1,line),end='')
"""
#145

"""spos=105
size=500

f=open('stockcode','r')
h=open('stockcode_part','w')

f.seek(spos)
data=f.read(size)
h.write(data)

h.close()
f.close()"""

#146
"""from os.path import getsize

file1='stockcode'
file2= 'img_sample.jpg'
file_size1=getsize(file1)
file_size2=getsize(file2)

print('File Name:%s \tFile Size:%d'%(file1,file_size1))
print('File Name:%s \tFile Size:%d'%(file2,file_size2))
"""
#147
from os import remove 

target_file='stockcode_copy.txt'
k=input('[%s] 파일을 삭제하겠습니까?(y/n)'%target_file)
if k=='y':
  remove(target_file)
  print('[%s]를 삭제했습니다.'%target_file)