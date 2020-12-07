class Bag:
	rules = {}
	bags = {}

	def __init__(self, color, required_contents=None):
		self.color = color
		self.required_contents = {}
		if required_contents is not None:
			self.required_contents = required_contents
	def __repr__(self):
		return '%s bags contain %s' % (self.color,self.required_contents)

	def can_contain(self,color):
		if self.required_contents.has_key(color):
			return True
		else:
			for bag_color in self.required_contents:
				if bags[bag_color].can_contain(color):
					return True
		return False

	def num_contains(self):
		number_bags_inside = 0
		for color, number in self.required_contents.items():
			number_bags_inside += number + number * bags[color].num_contains()
		return number_bags_inside

# placing the rows from the input file into a list
with open('input-1') as input_file:
	rules_file = input_file.readlines()


rules = {}
bags = {}
for rule_line in rules_file:
	split_rule = rule_line.rstrip().split(' bags contain ')
	color = split_rule[0]
	required_contents_list = split_rule[1][:-1].split(', ')
	required_contents = {}
	if required_contents_list[0] != 'no other bags':
		for content in required_contents_list:
			split_content = content.split(' ', 1)
			content_number = int(split_content[0])
			content_color = split_content[1][:-4] if content_number == 1 else split_content[1][:-5]
			required_contents[content_color] = content_number
	bags[color] = Bag(color,required_contents)
	rules[color] = required_contents

Bag.rules = rules
Bag.bags = bags

print bags['shiny gold'].num_contains()