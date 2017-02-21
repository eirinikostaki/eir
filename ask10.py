import urllib2
import json
import sys

data = raw_input("Dialexte ta nomismata Xwrismena me komma: USD,EUR,CNY (ignore case) \n")

internet = urllib2.urlopen('https://www.cryptocompare.com/api/data/price?fsym=BTC&tsyms=%s'%data)
html = internet.read()
draws=json.loads(html)["Data"]
clues = []

if not draws:
	print 'wrong input or syntax:"', data,'"'
	sys.exit(-1)

for d in draws:	
    clues +=d['Price'],d['Symbol']

numbers = []
run = len(clues) 

#se auth th for trexoume olo to pinaka clues(perigrafete h domi panw apo thn getCoin ).Afou oi ajies
#briskontai se arties 8eseis 0,2 klp sth for leme an i%2 != 0 einai peritto opote continue alliws 
#pros8etei thn timh ston pinaka numbers
#sth list numbers kratame oles tis ajies ton nomismatwn pou zhthse o xrhsths ( unsorted arxika)
for i in range (run):
	if i%2:
		continue
	numbers.append(clues[i])

sortedNumbers = sorted(numbers) #  sortedNumber = oi times me aujousa timh

#Ston pinaka clues exoume thn ejhs domi:
#ajia,nomisma,ajia,nomisma px:  100,eur,200,usd,300,gbp,50,cny
#opote h getCoin pairnei orisma thn ajia thn briskei sto clues kai epistrefei  
#to epomeno stoixeio pou 8a einai to onoma.px An parei orisma 200 pou einai to clues[2]
#8a kanei return to clues[3] pou einai to usd.
def getCoin(value):
	j = 1
	for i in range(len(clues)):
		if clues[i] is value:
			return clues[j]
		j+=1

final = []

#sto list final vazoume tous sortedNumber me thn seira 
#kai xrhsimopoiontas thn getCoin() dipla vazoume kai to onoma tou nomismatos.
#px sto parapanw paradeigma prwto 8a bei to sortedNumber[0] pou einai to 100
#8a kalesoume to getCoin(sortedNumber[0]) kai opws perigraftike parapanw 8a epistrepsei
# to eur kai sunexizei  h for gia sortedNumbers[1] klp 
for i in range(len(sortedNumbers)):
	final.append(sortedNumbers[i])
	final.append(getCoin(sortedNumbers[i]))

print str(final)
