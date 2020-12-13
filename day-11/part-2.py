import time

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
	time.sleep(.1)
	print pretty_layout(seat_layout)
	next_seat_layout = [x[:] for x in seat_layout]
	position_x = 0
	position_y = 0

	occupied_seats = 0

	while position_y < len(seat_layout):
		while position_x < len(seat_layout[0]):
			visible_seats = { 'L' : 0, '#' : 0 }

			# above and left
			y = -1
			x = -1
			# while the square is valid
			while(position_y + y >= 0 and position_x + x >= 0):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y -= 1
				x -= 1


			# above
			y = -1
			x = 0
			# while the square is valid
			while(position_y + y >= 0):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y -= 1

			# above and right
			y = -1
			x = 1
			# while the square is valid
			while(position_y + y >= 0 and position_x + x < len(seat_layout[0])):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y -= 1
				x += 1

			# left
			y = 0
			x = -1
			# while the square is valid
			while(position_x + x >= 0):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				x -= 1

			#right
			y = 0
			x = 1
			# while the square is valid
			while(position_x + x < len(seat_layout[0])):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				x += 1

			#below and left
			y = 1
			x = -1
			# while the square is valid
			while(position_y + y < len(seat_layout) and position_x + x >= 0):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y += 1
				x -= 1

			#below
			y = 1
			x = 0
			# while the square is valid
			while(position_y + y < len(seat_layout)):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y += 1

			# below and right
			y = 1
			x = 1
			# while the square is valid
			while(position_y + y < len(seat_layout) and position_x + x < len(seat_layout[0])):
				visible_tile = seat_layout[position_y + y][position_x + x]
				if visible_tile != '.':
					visible_seats[visible_tile] += 1
					break
				y += 1
				x += 1

			# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
			if seat_layout[position_y][position_x] == 'L' and visible_seats['#'] == 0:
				next_seat_layout[position_y][position_x] = '#'
				seats_changed += 1
			# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
			elif seat_layout[position_y][position_x] == '#' and visible_seats['#'] >= 5:
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