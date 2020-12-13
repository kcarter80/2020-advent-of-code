# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

instructions = []
for input_line in input_lines:
	instructions.append(input_line.rstrip())

facing = 0
position = [0,0]

print position
# casting each item in the list to an int
for i in range(0, len(instructions)):
	action = instructions[i][:1]
	magnitude = int(instructions[i][1:])

	#Action N means to move north by the given value.
	#Action S means to move south by the given value.
	#Action E means to move east by the given value.
	#Action W means to move west by the given value.
	#Action L means to turn left the given number of degrees.
	#Action R means to turn right the given number of degrees.
	#Action F means to move forward by the given value in the direction the ship is currently facing.
	if action == 'N':
		position[1] += magnitude
	elif action == 'S':
		position[1] -= magnitude
	elif action == 'E':
		position[0] += magnitude
	elif action == 'W':
		position[0] -= magnitude
	elif action == 'L':
		facing -= magnitude
		if facing < 0:
			facing += 360
	elif action == 'R':
		facing += magnitude
		if facing >= 360:
			facing -= 360
	elif action == 'F':
		if facing == 0:
			position[0] += magnitude
		elif facing == 90:
			position[1] -= magnitude
		elif facing == 180:
			position[0] -= magnitude
		elif facing == 270:
			position[1] += magnitude

	print position

print abs(position[0]) + abs(position[1])