def parse_boarding_pass_string(boarding_pass_string):
	row  = int(boarding_pass_string[ 0 : 7 ].replace('B','1').replace('F','0'),2)
	column = int(boarding_pass_string[ 7 : 10 ].replace('R','1').replace('L','0'),2)
	return { 'row': row, 'column': column}

def seat_id(boarding_pass):
	return boarding_pass['row'] * 8 + boarding_pass['column']

# placing the rows from the input file into a list
with open('input-1') as input_file:
	boarding_pass_strings = input_file.readlines()

boarding_pass_ids = []
for i in range(0, len(boarding_pass_strings)):
	boarding_pass_ids.append(seat_id(parse_boarding_pass_string(boarding_pass_strings[i].rstrip())))

boarding_pass_ids.sort()

i = 1
while i < len(boarding_pass_ids) - 2:
	if boarding_pass_ids[i+1] != boarding_pass_ids[i] + 1:
		break
	else:
		i += 1

print boarding_pass_ids[i] + 1