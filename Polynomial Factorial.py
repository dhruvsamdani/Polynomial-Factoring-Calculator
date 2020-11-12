def factor(n):
	list = []
	n=abs(n)
	for x in range(1, int(n)+1):
		if (n % x == 0):
			list.append(n/x)
			list.append(-n/x)
	return list
	
def evaluate(equation, value):
	num = 0
	for i in range(len(equation)):
		exp = (len(equation) - 1) - i
		num += equation[i]*value**exp
	return num

# RATIONAL ROOT THEOREM
def factors(eq):
	num = []
	x = factor(eq[-1])
	y = factor(eq[0])
	for i in x:
		for r in y:
			if (evaluate(eq,i/r) == 0):
				return(i/r)

def syntheticDivision(factors, equation):
	syntheticResults=[]
	current = 0
	for x in range(len(equation)):
		current = (current * factors) + equation[x] 
		syntheticResults.append(current)
	return syntheticResults[:-1]

def factorize(eq):
	facts = factors(eq)
	answer = []
	while facts:
		answer.append([1,-facts]) 
		eq = syntheticDivision(facts, eq)
		facts = factors(eq)
	return(answer)
eq = input('Please enter an equation in format a,b,c: ')
eq = [int(i) for i in eq.split(',')]
print(factorize(eq))