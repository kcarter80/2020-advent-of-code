spoken_numbers = {0: [1], 3: [2], 6: [3]}
last_number_spoken = 6
turn = 3

spoken_numbers = {1: [1], 3: [2], 2: [3]}
last_number_spoken = 2
turn = 3

spoken_numbers = {2: [1], 1: [2], 3: [3]}
last_number_spoken = 3
turn = 3

spoken_numbers = {1: [1], 2: [2], 3: [3]}
last_number_spoken = 3
turn = 3

spoken_numbers = {2: [1], 3: [2], 1: [3]}
last_number_spoken = 1
turn = 3

spoken_numbers = {3: [1], 2: [2], 1: [3]}
last_number_spoken = 1
turn = 3

spoken_numbers = {3: [1], 1: [2], 2: [3]}
last_number_spoken = 2
turn = 3

spoken_numbers = {15: [1], 12: [2], 0: [3], 14: [4], 3: [5], 1: [6]}
last_number_spoken = 1
turn = 6

while turn != 30000000:
	if turn % 1000000:
		print turn
	turn += 1
	if spoken_numbers.has_key(last_number_spoken) and len(spoken_numbers[last_number_spoken]) == 2:
		last_number_spoken = spoken_numbers[last_number_spoken][1] - spoken_numbers[last_number_spoken][0]
	else:
		last_number_spoken = 0
	if spoken_numbers.has_key(last_number_spoken):
		spoken_numbers[last_number_spoken].append(turn)
		if len(spoken_numbers[last_number_spoken]) == 3:
			spoken_numbers[last_number_spoken].pop(0)
	else:
		spoken_numbers[last_number_spoken] = [turn]

print last_number_spoken