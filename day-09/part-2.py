# placing the rows from the input file into a list
with open('input-1') as input_file:
	data_lines = input_file.readlines()

data = []
for data_line in data_lines:
	data.append(int(data_line.rstrip()))

invalid_number = 552655238
#invalid_number = 127

for i in range(0, len(data)-1):
	sum = data[i] + data[i+1]
	ii = i + 2
	while sum != invalid_number and sum < invalid_number:
		sum += data[ii]
		ii += 1
		if sum == invalid_number:
			if data[i] < data[i+1]:
				maximum = data[i+1]
				minimum = data[i]
			else:
				minimum = data[i+1]
				maximum = data[i]
			for iii in range(i+2,ii):
				if data[iii] > maximum:
					maximum = data[iii]
				if data[iii] < minimum:
					minimum = data[iii]
			print(minimum,maximum,minimum+maximum)