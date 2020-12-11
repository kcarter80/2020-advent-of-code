def pretty_layout(seat_layout):
	pretty_string = ''
	for i in range(0, len(seat_layout)):
		pretty_string += ''.join(seat_layout[i]) + '\n'
	return pretty_string

def round(seat_layout):
	seats_changed = 0
	return seats_changed

# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

seat_layout = [''] * len(input_lines)

for i in range(0, len(input_lines)):
	seat_layout[i] = list(input_lines[i].rstrip())

seats_changed = None

while seats_changed != 0:
	seats_changed = 0
	print pretty_layout(seat_layout)
	next_seat_layout = [x[:] for x in seat_layout]
	position_x = 0
	position_y = 0

	occupied_seats = 0

	while position_y < len(seat_layout):
		while position_x < len(seat_layout[0]):
			adjacents = { 'L' : 0, '#' : 0, '.' : 0}

			for y_adjustment in range(-1, 2):
				for x_adjustment in range(-1, 2):
					y_to_evaluate = position_y + y_adjustment
					x_to_evaluate = position_x + x_adjustment
					# don't evaluate self
					if not (x_adjustment == 0 and y_adjustment == 0):
						# if this is an in bounds tile
						if y_to_evaluate > -1 and y_to_evaluate < len(seat_layout) and x_to_evaluate > -1 and x_to_evaluate < len(seat_layout[0]):
							#print('yte',y_to_evaluate,'xte',x_to_evaluate)
							adjacents[seat_layout[y_to_evaluate][x_to_evaluate]] += 1
						# out of bounds
						else:
							# so is "floor"
							adjacents['.'] += 1
			#print position_y, position_x, adjacents

			# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
			if seat_layout[position_y][position_x] == 'L' and adjacents['#'] == 0:
				next_seat_layout[position_y][position_x] = '#'
				seats_changed += 1
			# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
			elif seat_layout[position_y][position_x] == '#' and adjacents['#'] >= 4:
				next_seat_layout[position_y][position_x] = 'L'
				seats_changed += 1
			if next_seat_layout[position_y][position_x] == '#':
				occupied_seats += 1
			position_x += 1	
		position_x = 0
		position_y += 1
	seat_layout = next_seat_layout

	print seats_changed

print 'all done'
print occupied_seats