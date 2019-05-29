def minutes_to_hours(minutes,seconds = 0.0):
	return int(minutes) / 60 + seconds/3600

# minutes=input("Enter minutes to convert : ")
# print(str(minutes_to_hours(minutes)) + " hours")

# print(minutes_to_hours(70,300))

def Celsius_to_Fahrenheit(temp_in_Celsius):
	return float(temp_in_Celsius) * 9 / 5 + 32


temperature = input("Enter the temperature in Celsius : ")
if float(temperature) < -273.15:
	print (" The lowest possible temperature that physical matter can reach is -273.15C")
else:
	temperature_in_Fahrenheit=Celsius_to_Fahrenheit(temperature)
	print(temperature +  " degree Celsius = " + str(temperature_in_Fahrenheit) + " Fahrenheit")

# def Length_of_string(s):
# 	try:
# 		return len(s)
# 	except:
# 		return "Sorry integers has no length"


def Length_of_string(s):
	if type(s)==int:
		return "Sorry integers has no length"
	else:
		return len(s)

# print(Length_of_string("Hello"))
# print(Length_of_string("Hello world"))