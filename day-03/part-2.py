# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_map = input_file.readlines()

tree_map = [''] * len(input_map)

for i in range(0, len(input_map)):
	tree_map[i] = list(input_map[i].rstrip())

position_x = 0
position_y = 0
trees = 0

def how_many_trees(input_map,movement_x,movement_y):
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

		if tree_map[position_y][position_x] == '#':
			trees += 1

		position_x += movement_x
		position_y += movement_y

	return trees

print(how_many_trees(input_map,1,1)*how_many_trees(input_map,3,1)*how_many_trees(input_map,5,1)*how_many_trees(input_map,7,1)*how_many_trees(input_map,1,2))