from collections import OrderedDict

def print_state(state):
	for z in state.keys():
		print('z=%s' % z)
		for y in state[z].keys():
			x_string = ''
			for x in state[z][y].keys():
				x_string += state[z][y][x]
			print(x_string)
		print('')

def add_buffer(state):
	existing_z_keys = list(state.keys())
	existing_x_and_y_keys = list(state[0].keys())
	new_z_keys = [existing_z_keys[0] - 1, existing_z_keys[len(existing_z_keys) - 1] + 1]
	new_x_and_y_keys = [existing_x_and_y_keys[0] - 1, existing_x_and_y_keys[len(existing_x_and_y_keys) - 1] + 1]
	all_x_and_y_keys = [new_x_and_y_keys[0]] + existing_x_and_y_keys + [new_x_and_y_keys[1]]
	for z in new_z_keys:
		state[z] = OrderedDict()
		for y in all_x_and_y_keys:
			state[z][y] = OrderedDict()
			for x in all_x_and_y_keys:
				state[z][y][x] = '.'
	# re-sort zs
	state = OrderedDict(sorted(state.items(), key=lambda item: item))
	for z in existing_z_keys:
		for y in new_x_and_y_keys:
			state[z][y] = OrderedDict()
			for x in all_x_and_y_keys:
				state[z][y][x] = '.'
		for y in existing_x_and_y_keys:
			for x in new_x_and_y_keys:
				state[z][y][x] = '.'
			# re-sort xs
			state[z][y] = OrderedDict(sorted(state[z][y].items(), key=lambda item: item))
		# re-sort ys
		state[z] = OrderedDict(sorted(state[z].items(), key=lambda item: item))
	return state

def position_value(z,y,x,state):
	if z in state.keys():
		if y in state[z].keys():
			if x in state[z][y].keys():
				return state[z][y][x]
	return '.'

def blank_rectangular_prism(state):
	blank_rectangular_prism = OrderedDict()
	for z in state.keys():
		blank_rectangular_prism[z] = OrderedDict()
		for y in state[z].keys():
			blank_rectangular_prism[z][y] = OrderedDict()
			for x in state[z][y].keys():
				blank_rectangular_prism[z][y][x] = '.'
	return blank_rectangular_prism

def do_turn(state):
	next_state = blank_rectangular_prism(state)
	for z in state.keys():
		for y in state[z].keys():
			for x in state[z][y].keys():
				# this will hit every coordinate, now need to count neighbors
				active_neighbors = 0
				evaluated_points = 0
				for z_to_evaluate in range(z-1, z+2): 
					for y_to_evaluate in range(y-1, y+2):
						for x_to_evaluate in range(x-1, x+2):
							if z_to_evaluate != z or y_to_evaluate != y or x_to_evaluate != x:
								evaluated_points += 1
								if position_value(z_to_evaluate,y_to_evaluate,x_to_evaluate,state) == '#':
									active_neighbors += 1
				# print(evaluated_points)
				if state[z][y][x] == '#':
					if active_neighbors == 2 or active_neighbors == 3:
						next_state[z][y][x] = '#'
					else:
						next_state[z][y][x] = '.'
				else:
					if active_neighbors == 3:
						next_state[z][y][x] = '#'
					else:
						next_state[z][y][x] = '.'
	return next_state

def count_active(state):
	active_count = 0
	for z in state.keys():
		for y in state[z].keys():
			for x in state[z][y].keys():
				if state[z][y][x] == '#':
					active_count += 1
	return active_count

state = OrderedDict()
state[0] = OrderedDict()
state[0][0] = OrderedDict({0:'.',1:'#',2:'.'})
state[0][1] = OrderedDict({0:'.',1:'.',2:'#'})
state[0][2] = OrderedDict({0:'#',1:'#',2:'#'})

'''
##...#.#
#..##..#
..#.####
.#..#...
########
######.#
.####..#
.###.#..
'''

state = OrderedDict()
state[0] = OrderedDict()
state[0][0] = OrderedDict({0:'#',1:'#',2:'.',3:'.',4:'.',5:'#',6:'.',7:'#'})
state[0][1] = OrderedDict({0:'#',1:'.',2:'.',3:'#',4:'#',5:'.',6:'.',7:'#'})
state[0][2] = OrderedDict({0:'.',1:'.',2:'#',3:'.',4:'#',5:'#',6:'#',7:'#'})
state[0][3] = OrderedDict({0:'.',1:'#',2:'.',3:'.',4:'#',5:'.',6:'.',7:'.'})
state[0][4] = OrderedDict({0:'#',1:'#',2:'#',3:'#',4:'#',5:'#',6:'#',7:'#'})
state[0][5] = OrderedDict({0:'#',1:'#',2:'#',3:'#',4:'#',5:'#',6:'.',7:'#'})
state[0][6] = OrderedDict({0:'.',1:'#',2:'#',3:'#',4:'#',5:'.',6:'.',7:'#'})
state[0][7] = OrderedDict({0:'.',1:'#',2:'#',3:'#',4:'.',5:'#',6:'.',7:'.'})

i=0
print(count_active(state))
print_state(state)
while (i<=5):
	state = add_buffer(state)
	state = do_turn(state)
	print(count_active(state))
	i += 1