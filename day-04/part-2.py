# takes a string of space separated, colon separated key/value pairs and returns key value pairs in a dictionary
def parse_passport(passport_string):
	split_passport = passport_string.split(' ')
	passport = {}
	for i in range(0, len(split_passport)):
		split_tuple = split_passport[i].split(':')
		passport[split_tuple[0]] = split_tuple[1]
	return passport

# The expected fields are as follows:
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.
def validate_passport(passport):
	if not (passport.has_key('byr') and passport.has_key('iyr') and passport.has_key('eyr') and passport.has_key('hgt')
		and passport.has_key('hcl') and passport.has_key('ecl') and passport.has_key('pid')):
		print -1
		return False

	if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
		print 0
		return False
	if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
		print 1
		return False
	if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
		print 2
		return False
	if passport['hgt'][-2:] != 'cm' and passport['hgt'][-2:] != 'in':
		print 3
		return False
	else:
		height_amount = int(passport['hgt'][:len(passport['hgt']) - 2])
		if passport['hgt'][-2:] == 'cm' and (height_amount > 193 or height_amount < 150):
			print 4
			return False
		elif passport['hgt'][-2:] == 'in':
			if (height_amount > 76 or height_amount < 59):
				print 5
				return False
	if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
		print 6
		return False
	allowed = list('0123456789abcdef')
	if (passport['hcl'][1] not in allowed or passport['hcl'][2] not in allowed or passport['hcl'][3] not in allowed or 
		passport['hcl'][4] not in allowed or passport['hcl'][5] not in allowed or passport['hcl'][6] not in allowed):
		print 7
		return False
	if (passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']):
		print 8
		return False
	if (len(passport['pid']) != 9):
		print 9
		return False
	allowed = list('0123456789')
	if (passport['pid'][0] not in allowed or passport['pid'][1] not in allowed or passport['pid'][2] not in allowed or 
		passport['pid'][3] not in allowed or passport['pid'][4] not in allowed or passport['pid'][5] not in allowed or 
		passport['pid'][6] not in allowed or passport['pid'][7] not in allowed or passport['pid'][8] not in allowed):
		print 10
		return False
	
	print 11
	return True

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
