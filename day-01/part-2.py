# placing the rows from the input file into a list
with open('input-1') as input_file:
    expenses = input_file.readlines()

# casting each item in the list to an int
for i in range(0, len(expenses)): 
    expenses[i] = int(expenses[i])

# if the entries sum to 2020 print their multiplation
for i in range(0, len(expenses)): 
    for ii in range(i, len(expenses)):
    	for iii in range(i, len(expenses)):
    		# don't allow repeats
    		if ii != iii:
    			if expenses[i] + expenses[ii] + expenses[iii] == 2020:
    				#TODO: break out so it doesn't print twice
    				print(expenses[i] * expenses[ii] * expenses[iii])
