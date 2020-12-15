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
		floats = []
		for i in reversed(range(0, 36)):
			if value[i] == 'X':
				floats.append(i)
			elif value[i] == '1':
				ones.append(i)
		print ones,floats
	else:
		address = int(instruction.split('[')[1].split(']')[0])
		value = int(value)
		binary_address_list = list('{0:036b}'.format(address))
		#print 'before',''.join(binary_value_string)
		for i in ones:
			binary_address_list[i] = '1'
		for i in floats:
			binary_address_list[i] = 'X'

		addresses = []
		if len(floats) == 0:
			addresses.append(''.join(binary_address_list))
		else:
			# the length of the floats is the number of binary digits of float combos
			for i in range(0, 2 ** len(floats)):
				format_string = '{0:0' + str(len(floats)) +'b}'
				float_combo = list(format_string.format(i))
				address = list(binary_address_list)
				for ii in range(0, len(float_combo)):
					address[floats[ii]] = float_combo[ii]
				print float_combo,'address',''.join(address)
				addresses.append(''.join(address))

		for address in addresses:
			mem[int(''.join(address),2)] = value

print mem

print sum(mem.values())