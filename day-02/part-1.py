# placing the rows from the input file into a list
with open('input-1') as input_file:
	passwords = input_file.readlines()

valid_passwords = 0

for i in range(0, len(passwords)):
	passwords[i] = passwords[i].rstrip()
	# e.g.: 5-12 s: sgscssssphxs
	minimum = int(passwords[i].split('-')[0])
	maximum = int(passwords[i].split(' ')[0].split('-')[1])
	letter = passwords[i].split(' ')[1].split(':')[0]
	password = passwords[i].split(': ')[1]

	if password.count(letter) >= minimum and password.count(letter) <= maximum:
		valid_passwords += 1

print valid_passwords