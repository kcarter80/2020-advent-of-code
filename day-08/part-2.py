def run_program(program):
	acc = 0
	line_to_execute = 0
	executed_lines = {}
	while line_to_execute < len(program):
		if executed_lines.has_key(line_to_execute):
			print('infinite loop',acc)
			return False
		else:
			executed_lines[line_to_execute] = True
		if program[line_to_execute][0] == 'acc':
			acc += program[line_to_execute][1]
			line_to_execute += 1
		elif program[line_to_execute][0] == 'jmp':
			line_to_execute += program[line_to_execute][1]
		elif program[line_to_execute][0] == 'nop':
			line_to_execute += 1 
		else:
			print 'unknown instruction'
	if line_to_execute == len(program):
		print('successfully terminated',acc)
		return True


# placing the rows from the input file into a list
with open('input-1') as input_file:
	program_lines = input_file.readlines()

program = []
for program_line in program_lines:
	split_program_line = program_line.rstrip().split(' ')
	program.append([split_program_line[0], int(split_program_line[1])])

instruction_index = 0
successful = False
while not successful:
	if program[instruction_index][0] == 'nop':
		program[instruction_index][0] = 'jmp'
		successful = run_program(program)
		program[instruction_index][0] = 'nop'
	elif program[instruction_index][0] == 'jmp':
		program[instruction_index][0] = 'nop'
		successful = run_program(program)
		program[instruction_index][0] = 'jmp'
	instruction_index += 1