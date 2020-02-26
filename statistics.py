import math

##########################################
#        created by @torokoko            #
#              torokoko.cl               #
##########################################

#This program is designed to get the basic fuctions of statistics
#Some variables may be in spanish because is my native language, i'm sorry :(

numbers = []

print('Enter numbers, press enter for each number and when you are finish press any key and enter')

#this makes a loop until you don't want to enter more numbers
while True:
	try:
		xnum = int(input())

		numbers.append(xnum)
	except ValueError:
		break

sorted = sorted(numbers)
def average(numbers):
	sum_num = 0
	for i in numbers:
		sum_num = sum_num + i
	avg = sum_num / len(numbers)
	return avg
avg = average(numbers)
print('average: ' + str(avg))

#Variance

def variance(numbers):
	x = 0
	for i in numbers:
		x = x + (i - avg)**2
	var = x / (len(numbers) - 1)
	return var
var = variance(numbers)
print('variance: ' + str(var))

#Standar Deviation

desv = math.sqrt(var)
print('standard deviation: ' + str(desv))	

#Range

n_smaller = sorted[0]
n_bigger = sorted[-1]

range = n_bigger - n_smaller
print('range:' + str(range))
