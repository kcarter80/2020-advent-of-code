def parse_boarding_pass_string(boarding_pass_string):
	row  = int(boarding_pass_string[ 0 : 7 ].replace('B','1').replace('F','0'),2)
	column = int(boarding_pass_string[ 7 : 10 ].replace('R','1').replace('L','0'),2)
	return { 'row': row, 'column': column}

def seat_id(boarding_pass):
	return boarding_pass['row'] * 8 + boarding_pass['column']

# placing the rows from the input file into a list
with open('input-1') as input_file:
	boarding_pass_strings = input_file.readlines()

highest_seat_id = 0
for i in range(0, len(boarding_pass_strings)):
	this_seat_id = seat_id(parse_boarding_pass_string(boarding_pass_strings[i].rstrip()))
	if this_seat_id > highest_seat_id:
		highest_seat_id = this_seat_id

print highest_seat_id