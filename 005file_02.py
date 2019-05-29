# file=open('fruits.txt','r')

# # content=file.read()
# # file.close()

# # print(content)

# content=file.readlines()
# file.close()

# # for line in content:
# # 	print(line)
# # 	print(len(line)-1) # the last char is \n


# for line in content:
# 	print(len(line.strip()))


# numbers=[1,2,3,4]

# file=open('numbers.txt','w')
# for i in numbers:
# 	file.write(str(i)+'\n')

# file.close()


temperatures=[20,-20,-289,100]

def tempWriter(temp,file):
	f=open(file,'w')
	for t in temp:
		if t>-273.15:
			tf=t *9/5+32;
			f.write(str(tf)+'\n')
	f.close()

tempWriter(temperatures,'result.txt')