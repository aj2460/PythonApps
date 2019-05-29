# raw text r"""


r"""
This scripts creeate an empty file
"""
def create_file(filename):
	"""This function create an empty file"""
	with open(filename,'w') as file:
		file.write("")


create_file("hello.txt")


import doc
print(doc.__doc__)
print(doc.create_file.__doc__)
