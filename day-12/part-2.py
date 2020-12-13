# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

instructions = []
for input_line in input_lines:
	instructions.append(input_line.rstrip())

ship_position = [0,0]
waypoint = [10,1]

print ship_position
# casting each item in the list to an int
for i in range(0, len(instructions)):
	action = instructions[i][:1]
	magnitude = int(instructions[i][1:])

	#Action N means to move the waypoint north by the given value.
	#Action S means to move the waypoint south by the given value.
	#Action E means to move the waypoint east by the given value.
	#Action W means to move the waypoint west by the given value.
	#Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
	#Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
	#Action F means to move forward to the waypoint a number of times equal to the given value.
	if action == 'N':
		waypoint[1] += magnitude
	elif action == 'S':
		waypoint[1] -= magnitude
	elif action == 'E':
		waypoint[0] += magnitude
	elif action == 'W':
		waypoint[0] -= magnitude
	elif action == 'L':
		waypoint_x = waypoint[0]
		waypoint_y = waypoint[1]
		if magnitude == 270:
			waypoint[0] = waypoint_y
			waypoint[1] = -waypoint_x
		elif magnitude == 180:
			waypoint[0] = -waypoint_x
			waypoint[1] = -waypoint_y
		elif magnitude == 90:
			waypoint[0] = -waypoint_y
			waypoint[1] = waypoint_x
	elif action == 'R':
		waypoint_x = waypoint[0]
		waypoint_y = waypoint[1]
		if magnitude == 90:
			waypoint[0] = waypoint_y
			waypoint[1] = -waypoint_x
		elif magnitude == 180:
			waypoint[0] = -waypoint_x
			waypoint[1] = -waypoint_y
		elif magnitude == 270:
			waypoint[0] = -waypoint_y
			waypoint[1] = waypoint_x
	elif action == 'F':
		ship_position[0] += waypoint[0] * magnitude
		ship_position[1] += waypoint[1] * magnitude
	print ship_position

print abs(ship_position[0]) + abs(ship_position[1])