a = map(int, raw_input("dwse mia seira arithmwnh opou tha periexodai mhdenika me keno anamesa tous:").split())
#kanei iterate thn lista kai an brei zero to diagrafei kai tautoxrona kanei 
#appent ena mhdeniko sto telos
zeros = []
nums = []
for i in range (len(a)):
	if not a[i]:
		zeros.append(0)
	if a[i]:
		nums.append(a[i])

final = nums + zeros

print final