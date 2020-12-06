# placing the rows from the input file into a list
with open('input-1') as input_file:
	collected_answers = input_file.readlines()

# list of all the groups' answers 
groups_answers = []
# a single group's answers
group_answers = {}
# the number of members in a group
group_members = 0
# the puzzle answer
everyone_answered_sum = 0
for i in range(0, len(collected_answers)):
	# new group
	if collected_answers[i] == '\n':
		groups_answers.append(group_answers)
		print (group_members,group_answers.items())
		for question, num_answers in group_answers.items():
			if num_answers == group_members:
				everyone_answered_sum += 1
		group_members = 0
		group_answers = {}
	# same group
	else:
		split_answers = list(collected_answers[i].rstrip())
		for ii in range(0, len(split_answers)):
			# The get function can be used to initialize a non-existing key
			# or to increment if it exists
			group_answers[split_answers[ii]] = group_answers.get(split_answers[ii], 0) + 1
		group_members += 1

# make sure we get the last one in there
groups_answers.append(group_answers)
for question, num_answers in group_answers.items():
	if num_answers == group_members:
		everyone_answered_sum += 1
print groups_answers
print everyone_answered_sum