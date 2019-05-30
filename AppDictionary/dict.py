import json
from  difflib import get_close_matches
# from  difflib import SequenceMatcher

data=json.load(open('data.json','r'))

def lookup(word):
	if word.capitalize() in data:
		return data[word.capitalize()]
	elif word.upper() in data:
		return data[word.upper()]
	else:
		word=word.lower()
		if word in data:
			return data[word]
		elif len(get_close_matches(word,data.keys())) >0:
			yn=input("Did you mean %s instead? Enter Y if yes or N if No: " % get_close_matches(word,data.keys())[0])
			if yn.lower()=='y':
				return data[get_close_matches(word,data.keys())[0]]
			elif yn.lower()=='n':
				return "The word doesn't exist. Please check it."
			else:
				return "We didn't understand the entry"
		else:
			return "Word not found"	

# print(data['rain'])
print("-"*30)
word=input("Enter the word too lookup : ")
output=lookup(word)
print("-"*30)

i=1
if type(output) == list:
	for item in output:
		print("(%s) %s" %(i,item))
		i=i+1;

else:
	print(output)
print("="*30)
