import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d") +".txt","w") as mainfile:
	for  file in filenames :
		with open(file,"r") as f:
			mainfile.write(f.read() + "\n")


