# placing the rows from the input file into a list
with open('input-1') as input_file:
	passwords = input_file.readlines()

valid_passwords = 0

for i in range(0, len(passwords)):
	passwords[i] = passwords[i].rstrip()
	# e.g.: 5-12 s: sgscssssphxs
	first_position = int(passwords[i].split('-')[0]) - 1
	second_position = int(passwords[i].split(' ')[0].split('-')[1]) - 1
	letter = passwords[i].split(' ')[1].split(':')[0]
	password = passwords[i].split(': ')[1]

	if (password[first_position] == letter and password[second_position] != letter) or (password[first_position] != letter and password[second_position] == letter):
		valid_passwords += 1

print valid_passwords