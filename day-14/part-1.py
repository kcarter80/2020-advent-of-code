# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

mem = {}
for input_line in input_lines:
	instruction = input_line.split(' = ')[0]
	value = input_line.split(' = ')[1]
	print instruction
	if instruction == 'mask':
		ones = []
		zeroes = []
		for i in reversed(range(0, 36)):
			if value[i] == '0':
				zeroes.append(i)
			elif value[i] == '1':
				ones.append(i)
		print ones,zeroes
	else:
		address = instruction.split('[')[1].split(']')[0]
		value = int(value)
		binary_value_list = list('{0:036b}'.format(value))
		#print 'before',''.join(binary_value_string)
		for i in zeroes:
			binary_value_list[i] = '0'
		for i in ones:
			binary_value_list[i] = '1'
		mem[address] = int(''.join(binary_value_list),2)
		print mem

print sum(mem.values())