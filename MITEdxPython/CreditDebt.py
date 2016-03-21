balance = float(raw_input('Enter the starting balance: '))
interest = float(raw_input('Enter the interest: '))
monthlyrate = float(raw_input('Enter the minimum monthly payment rate: '))
count = 0
sum = 0

def balanceCal(balance,monthlyrate):
	
	global count,interest,sum
	min = balance * monthlyrate
	unpaid = balance - min
	min = round(min,2)
	unpaid = round(unpaid,2)
	sum = sum + min
	count = count + 1
	print 'This is for the month of ' + str(count)
	print 'Minimum Monthly payment: ' + str(min)
	CalcInterest(unpaid,interest)

def CalcInterest(unpaid,interest):
	global sum
	global count,monthlyrate,balance
	
	newBalance = unpaid + ((interest/12.0) * unpaid)
	newBalance = round(newBalance,2)
	print 'The remaining balance is : ' +str(newBalance)	
	if count < 12:
		balanceCal(newBalance,monthlyrate)
	else:
		print 'Total Money Paid: ' + str(sum)
		print 'Total Remaining Balance is: ' + str(newBalance)
		 	
		exit()
	
balanceCal(balance,monthlyrate)
