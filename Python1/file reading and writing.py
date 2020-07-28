#file reading
'''
file=open('name.txt','r+')
print(file.writable())
text=file.read()
print(text)
size=len(text)
print(size)
li=file.readlines()
print(li)
for line in file:
 print(line)
file.close()
'''
#file writing
file=open('name.txt','a')
file.write("\nanis")
file=open('name1.txt','w')
file.write("\nanis")
file.close()