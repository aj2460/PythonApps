file=open('example_1.txt','w')

file.write("Line 1")
file.write("Line 2\n")
file.write("Line 3")

file.close()
file=open('example_1.txt','a')
file.write("Line 4\n")
file.close()


with open('example_1.txt','a+') as file:
	file.seek(0)
	content=file.readline()
	print(content)
	file.write('Line 6\n')

