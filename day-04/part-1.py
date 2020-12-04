# takes a string of space separated, colon separated key/value pairs and returns key value pairs in a dictionary
def parse_passport(passport_string):
	split_passport = passport_string.split(' ')
	passport = {}
	for i in range(0, len(split_passport)):
		split_tuple = split_passport[i].split(':')
		passport[split_tuple[0]] = split_tuple[1]
	return passport

# The expected fields are as follows:
#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)
def validate_passport(passport):
	return (passport.has_key('byr') and passport.has_key('iyr') and passport.has_key('eyr') and passport.has_key('hgt')
		and passport.has_key('hcl') and passport.has_key('ecl') and passport.has_key('pid'))

# placing the rows from the input file into a list
with open('input-1') as input_file:
	passports = input_file.readlines()

i = 0
valid_passports = 0
new_passport = True
while i < len(passports):
	passports[i] = passports[i].rstrip()
	if passports[i] == '':
		passports.pop(i)
		new_passport = True
		# at this point can parse the *last* passport
		passports[i-1] = parse_passport(passports[i-1])
		if validate_passport(passports[i-1]):
			valid_passports += 1
	else:
		if not new_passport:
			passports[i-1] += ' ' + passports[i]
			passports.pop(i)
		else:
			i += 1
		new_passport = False
# need to parse the final passport since it's not done by the while loop
passports[i-1] = parse_passport(passports[i-1])
if validate_passport(passports[i-1]):
	valid_passports += 1

print valid_passports
