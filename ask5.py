def printHasNumbers():
	print '***Harshad Numbers:***'
	i = 1
	number = []
	while(i < 1000):#trexei olous tour ari8mous
		if not i % sum(int(a) for a in str(i)):#an to sum diairei  to pros8etei sth lista
			number.append(i)
		i+=1
	return number
 
def printMulNumbers():
	print '***Diairounte me to ginomeno twm psifiwn tous:***'
	i = 1
	ginomeno = 1
	number = []
	while(i<1000): # trexei olous tous ari8mous mexri 1000
		for curr in str(i): # gia ton ekastote ari8mo pol/zei ta digit tou
			ginomeno *= int (curr)
		if ginomeno: #an den bgei zero
			if not i % ginomeno: # kai arithmos % ginome ==0
				number.append(i) 
		ginomeno = 1		
		i+=1
	return number

print ''.join(str(printHasNumbers()))
print ''.join(str(printMulNumbers()))
