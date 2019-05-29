import json
from  difflib import get_close_matches
# from  difflib import SequenceMatcher

data=json.load(open('data.json','r'))

def lookup(word):
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

word=input("Enter the word too lookup : ")
output=lookup(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)