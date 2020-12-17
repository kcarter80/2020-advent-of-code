# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

parse_phase = 0
rules = []
nearby_tickets = []
for input_line in input_lines:
	if input_line == '\n':
		parse_phase += 1
	else:
		if parse_phase == 0:
			split_line = input_line.rstrip().split(': ')[1].split(' ')
			range_1_start = int(split_line[0].split('-')[0])
			range_1_end = int(split_line[0].split('-')[1])
			range_2_start = int(split_line[2].split('-')[0])
			range_2_end = int(split_line[2].split('-')[1])
			rules.append([range_1_start,range_1_end,range_2_start,range_2_end])
		if parse_phase == 1:
			if input_line != 'your ticket:\n':
				my_ticket = input_line.rstrip().split(',')
				my_ticket = list(map(int, my_ticket)) 
		if parse_phase == 2:
			if input_line != 'nearby tickets:\n':
				nearby_tickets.append(input_line.rstrip().split(','))
				nearby_tickets[len(nearby_tickets) - 1] = list(map(int, nearby_tickets[len(nearby_tickets) - 1])) 

print rules
print my_ticket
print nearby_tickets
#[[1, 3, 5, 7], [6, 11, 33, 44], [13, 40, 45, 50]]
#[7, 1, 14]
#[[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]

ticket_scanning_error_rate = 0

for ticket in nearby_tickets:
	print ticket
	for value in ticket:
		passed_rule = False
		for rule in rules:
			print value, rule	
			if (value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3]):
				passed_rule = True
		if not passed_rule:
			ticket_scanning_error_rate += value

print ticket_scanning_error_rate