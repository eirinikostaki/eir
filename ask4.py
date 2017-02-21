import numpy
import sys
numbers = map(float, raw_input().split())

if len(numbers) is 4 or len(numbers) < 5: # prepei na diavasoume 5 ari8mous toulaxiston afou 4 diagrafontai
	sys.exit(-1)

def delMax():  # kanei delete ton megalutero ari8mo apo thn lista
	delete = max(numbers)
	for i in range(len(numbers)):
		if delete == numbers[i]:
			del numbers[i]
			break

def delMin(): # # kanei delete ton mikrotero ari8mo apo thn lista
	delete = min(numbers)
	for i in range(len(numbers)):
		if delete == numbers[i]:
			del numbers[i]
			break

# Briskei MO
def findAverage(): 
	tmp = 0
	for i in range(len(numbers)):
		tmp = tmp + numbers[i]
	return tmp/len(numbers)

#afairei ton MO apo ka8e ari8mo upswnei to result sto tetragwno 
#pros8etei ola ta results kai ta epistrefei
def findDiff(avg):
	totalDiff = 0
	for i in range(len(numbers)):
		tmp = (numbers[i]-avg)*(numbers[i]-avg)		
		totalDiff += tmp
	return totalDiff

delMin() 
delMin()
delMax() 
delMax()
avg = findAverage()
totalDiff = findDiff(avg)

#H tupikh apoklhsh einai h riza
#ths sunolikhs diaforas dia to plh8os ari8mwn

print numpy.sqrt(totalDiff/len(numbers))