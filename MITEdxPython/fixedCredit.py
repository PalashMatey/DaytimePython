balance = float(raw_input('Enter the starting balance: '))
interest = float(raw_input('Enter the interest: '))
count = 0
sum = 0
min = 100
def balanceCal(balance,min):
	global count,interest,sum
	
	unpaid = balance - min
	min = round(min,2)
	unpaid = round(unpaid,2)
	count = count + 1
	print 'This is for the month of ' + str(count)
	print 'Minimum Monthly payment: ' + str(min)
	CalcInterest(unpaid,interest)

def CalcInterest(unpaid,interest):
	global sum
	global count,balance,min
	
	newBalance = unpaid + ((interest/12.0) * unpaid)
	newBalance = round(newBalance,2)
	print 'The remaining balance is : ' +str(newBalance)	
	if count < 12:
		balanceCal(newBalance,min)
	else:
		if newBalance > 0:
			count = 0
			min = min + 10
			balanceCal(balance,min)
			print 'Total Money Paid: ' + str(sum)
			print 'Total Remaining Balance is: ' + str(newBalance)		 	
		else : 
			print 'Lowest Monthly payment: ' + str(min)
			exit()
	
balanceCal(balance,min)
