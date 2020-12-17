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
			rules.append({'name': input_line.split(': ')[0], 'ranges':{
				'range_1_start': range_1_start,
				'range_1_end': range_1_end,
				'range_2_start': range_2_start,
				'range_2_end': range_2_end
			}})
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

i = 0
while i < len(nearby_tickets):
	ticket = nearby_tickets[i]
	for value in ticket:
		passed_rule = False
		for rule in rules:
			if (value >= rule['ranges']['range_1_start'] and value <= rule['ranges']['range_1_end']) or (value >= rule['ranges']['range_2_start'] and value <= rule['ranges']['range_2_end']):
				passed_rule = True
		if not passed_rule:
			# discard invalid tickets
			nearby_tickets.pop(i)
			i -= 1
			# no need to evaluate future values
			break
	i += 1

print nearby_tickets
# we have all good nearby tickets now

position_passes_rules = []
total_positions_passing_rules = 0

# loop through each ticket field
for position in range(0, len(nearby_tickets[0])):
	position_passes_rules.append({'position': position, 'rules': []})
	rule_index = -1
	for rule in rules:
		print rule
		rule_index += 1
		ticket_position_failed_rule = False
		for ticket in nearby_tickets:
			print 'evaluating postion',position,'rule',rule_index,'value',ticket[position]
			if not ((ticket[position] >= rule['ranges']['range_1_start'] and ticket[position] <= rule['ranges']['range_1_end']) or (ticket[position] >= rule['ranges']['range_2_start'] and ticket[position] <= rule['ranges']['range_2_end'])):
				ticket_position_failed_rule = True
				break
		if ticket_position_failed_rule:
			print 'A rule was failed for this field.'
			# no need to continue this iteration, because this field already failed a rule. on to the next field.
			continue
		else:
			print 'All tickets passed all rules for this field.',position,rule_index
			position_passes_rules[len(position_passes_rules) - 1]['rules'].append(rule)

# A function that returns the number of rules for this position
def myFunc(e):
  return len(e['rules'])

position_passes_rules.sort(key=myFunc)

print position_passes_rules

i = 0
for i in range(0, len(position_passes_rules)):
	name_of_rule_to_pop = position_passes_rules[i]['rules'][0]['name']
	#print i,name_of_rule_to_pop
	for ii in range(i+1, len(position_passes_rules)): 
		print i,name_of_rule_to_pop
		iii = 0
		while iii < len(position_passes_rules[ii]['rules']):
			if position_passes_rules[ii]['rules'][iii]['name'] == name_of_rule_to_pop:
				position_passes_rules[ii]['rules'].pop(iii)
				print 'removing',name_of_rule_to_pop
				break
			iii += 1
		
print my_ticket

solution = 1
for position in position_passes_rules:
	if 'departure' in position['rules'][0]['name']:
		print position['rules'][0]['name'], position['position']
		solution *= my_ticket[position['position']]

print solution