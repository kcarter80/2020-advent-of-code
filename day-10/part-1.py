# placing the rows from the input file into a list
with open('input-1') as input_file:
	input_lines = input_file.readlines()

adapters = []
for input_line in input_lines:
	adapters.append(int(input_line.rstrip()))

adapters.sort()

# the last difference is always 3, so start at 1
jolt_differences = { 1:0, 2:0, 3:1}
# the first difference is the difference between 0 and the first adapater
jolt_differences[adapters[0]] += 1
for i in range(1, len(adapters)):
	difference = adapters[i] - adapters[i-1]
	jolt_differences[difference] += 1

print adapters
print jolt_differences
print jolt_differences[1] * jolt_differences[3]