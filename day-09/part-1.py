# placing the rows from the input file into a list
with open('input-1') as input_file:
	data_lines = input_file.readlines()

data = []
for data_line in data_lines:
	data.append(int(data_line.rstrip()))

preamble = 25

for index_to_evaluate in range(preamble, len(data)):
	found_valid_pair = False
	for i in range(index_to_evaluate - preamble, index_to_evaluate):
		for ii in range(index_to_evaluate - preamble + 1, index_to_evaluate):
			if data[i] + data[ii] == data[index_to_evaluate]:
				found_valid_pair = True
	print(found_valid_pair,data[index_to_evaluate])