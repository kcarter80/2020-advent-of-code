from collections import OrderedDict
import sys

def print_state(state):
	for w in state.keys():
		for z in state[w].keys():
			print('z=%s w=%s' %(z,w))
			for y in state[w][z].keys():
				x_string = ''
				for x in state[w][z][y].keys():
					x_string += state[w][z][y][x]
				print(x_string)
			print('')

def add_buffer(state):
	existing_w_and_z_keys = list(state.keys())
	existing_x_and_y_keys = list(state[0][0].keys())
	new_w_and_z_keys = [existing_w_and_z_keys[0] - 1, existing_w_and_z_keys[len(existing_w_and_z_keys) - 1] + 1]
	new_x_and_y_keys = [existing_x_and_y_keys[0] - 1, existing_x_and_y_keys[len(existing_x_and_y_keys) - 1] + 1]
	all_x_and_y_keys = [new_x_and_y_keys[0]] + existing_x_and_y_keys + [new_x_and_y_keys[1]]
	
	#print(existing_w_and_z_keys,existing_x_and_y_keys,new_w_and_z_keys,new_x_and_y_keys,all_x_and_y_keys)

	for w in new_w_and_z_keys + existing_w_and_z_keys:
		if not w in state: 
			state[w] = OrderedDict()
		for z in new_w_and_z_keys + existing_w_and_z_keys:
			if not z in state[w]:
				state[w][z] = OrderedDict()
				# these are new w and z dimensions, give blank x,y square canvasses
				for y in all_x_and_y_keys:
					state[w][z][y] = OrderedDict()
					for x in all_x_and_y_keys:
						#print('w is',w,'z is',z,'y is',y,'x is',x)
						state[w][z][y][x] = '.'
		# re-sort zs
		state[w] = OrderedDict(sorted(state[w].items(), key=lambda item: item))
	# re-sort ws
	state = OrderedDict(sorted(state.items(), key=lambda item: item))

	# these are existing x and z dimensions, fill x,y rim with '.'
	for w in existing_w_and_z_keys:
		for z in existing_w_and_z_keys:
			for y in new_x_and_y_keys:
				state[w][z][y] = OrderedDict()
				for x in all_x_and_y_keys:
					state[w][z][y][x] = '.'
			for y in existing_x_and_y_keys:
				for x in new_x_and_y_keys:
					state[w][z][y][x] = '.'
				# re-sort xs
				state[w][z][y] = OrderedDict(sorted(state[w][z][y].items(), key=lambda item: item))
			# re-sort ys
			state[w][z] = OrderedDict(sorted(state[w][z].items(), key=lambda item: item))
	return state

def position_value(w,z,y,x,state):
	if w in state.keys():
		if z in state[w].keys():
			if y in state[w][z].keys():
				if x in state[w][z][y].keys():
					return state[w][z][y][x]
	return '.'

def blank_rectangular_prism(state):
	blank_rectangular_prism = OrderedDict()
	for w in state.keys():
		blank_rectangular_prism[w] = OrderedDict()
		for z in state[w].keys():
			blank_rectangular_prism[w][z] = OrderedDict()
			for y in state[w][z].keys():
				blank_rectangular_prism[w][z][y] = OrderedDict()
				for x in state[w][z][y].keys():
					blank_rectangular_prism[w][z][y][x] = '.'
	return blank_rectangular_prism

def do_turn(state):
	next_state = blank_rectangular_prism(state)
	for w in state.keys():
		for z in state[w].keys():
			for y in state[w][z].keys():
				for x in state[w][z][y].keys():
					# this will hit every coordinate, now need to count neighbors
					active_neighbors = 0
					for w_to_evaluate in range(w-1, w+2):
						for z_to_evaluate in range(z-1, z+2): 
							for y_to_evaluate in range(y-1, y+2):
								for x_to_evaluate in range(x-1, x+2):
									if w_to_evaluate != w or z_to_evaluate != z or y_to_evaluate != y or x_to_evaluate != x:
										if position_value(w_to_evaluate,z_to_evaluate,y_to_evaluate,x_to_evaluate,state) == '#':
											active_neighbors += 1
					if state[w][z][y][x] == '#':
						if active_neighbors == 2 or active_neighbors == 3:
							next_state[w][z][y][x] = '#'
						else:
							next_state[w][z][y][x] = '.'
					else:
						if active_neighbors == 3:
							next_state[w][z][y][x] = '#'
						else:
							next_state[w][z][y][x] = '.'
	return next_state

def count_active(state):
	active_count = 0
	for w in state.keys():
		for z in state[w].keys():
			for y in state[w][z].keys():
				for x in state[w][z][y].keys():
					if state[w][z][y][x] == '#':
						active_count += 1
	return active_count

state = OrderedDict()
state[0] = OrderedDict()
state[0][0] = OrderedDict()
state[0][0][0] = OrderedDict({0:'.',1:'#',2:'.'})
state[0][0][1] = OrderedDict({0:'.',1:'.',2:'#'})
state[0][0][2] = OrderedDict({0:'#',1:'#',2:'#'})


state = OrderedDict()
state[0] = OrderedDict()
state[0][0] = OrderedDict()
state[0][0][0] = OrderedDict({0:'#',1:'#',2:'.',3:'.',4:'.',5:'#',6:'.',7:'#'})
state[0][0][1] = OrderedDict({0:'#',1:'.',2:'.',3:'#',4:'#',5:'.',6:'.',7:'#'})
state[0][0][2] = OrderedDict({0:'.',1:'.',2:'#',3:'.',4:'#',5:'#',6:'#',7:'#'})
state[0][0][3] = OrderedDict({0:'.',1:'#',2:'.',3:'.',4:'#',5:'.',6:'.',7:'.'})
state[0][0][4] = OrderedDict({0:'#',1:'#',2:'#',3:'#',4:'#',5:'#',6:'#',7:'#'})
state[0][0][5] = OrderedDict({0:'#',1:'#',2:'#',3:'#',4:'#',5:'#',6:'.',7:'#'})
state[0][0][6] = OrderedDict({0:'.',1:'#',2:'#',3:'#',4:'#',5:'.',6:'.',7:'#'})
state[0][0][7] = OrderedDict({0:'.',1:'#',2:'#',3:'#',4:'.',5:'#',6:'.',7:'.'})


i=0
while (i<=5):
	state = add_buffer(state)
	state = do_turn(state)
	print(count_active(state))
	i += 1