file=open('example.txt','r')
content=file.read()
print(content)

content1=file.readline()
print(content1)
file.seek(0)

content1=file.readline()
print(content1)


content2=file.readlines()
print(content2)

content3=[i.rstrip('\n') for i in content2]
print(content3)

for l in content3:
	print(l)

file.close()