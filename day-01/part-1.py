# placing the rows from the input file into a list
with open('input-1') as input_file:
    expenses = input_file.readlines()

# casting each item in the list to an int
for i in range(0, len(expenses)): 
    expenses[i] = int(expenses[i])

# if the entries sum to 2020 print their multiplation
for i in range(0, len(expenses)): 
    for ii in range(i, len(expenses)):
    	if expenses[i] + expenses[ii] == 2020:
    		print(expenses[i] * expenses[ii])
