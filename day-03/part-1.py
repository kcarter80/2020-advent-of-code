# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_map = input_file.readlines()

tree_map = [''] * len(input_map)

for i in range(0, len(input_map)):
	tree_map[i] = list(input_map[i].rstrip())

position_x = 0
position_y = 0
trees = 0

while position_y < len(tree_map):
	if position_x >= len(tree_map[0]):
		for i in range(0, len(input_map)):
			tree_map[i] += list(input_map[i].rstrip())

	print(position_x,position_y,tree_map[position_y][position_x] == '#')
	if tree_map[position_y][position_x] == '#':
		trees += 1

	position_x += 3
	position_y += 1

print(position_x,position_y,trees)
