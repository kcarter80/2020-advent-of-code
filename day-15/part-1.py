#umbers_spoken = [0,3,6] #436
#numbers_spoken = [1,3,2] #1
#numbers_spoken = [2,1,3] #10
#numbers_spoken = [1,2,3] #27
#numbers_spoken = [2,3,1] #78
#numbers_spoken = [3,2,1] #438
#numbers_spoken = [3,1,2] #1836
numbers_spoken = [15,12,0,14,3,1]
turn = 6

while turn != 2020:
	turn += 1
	# if the last number spoken appears more than once
	last_number_spoken = numbers_spoken[len(numbers_spoken) - 1]
	if numbers_spoken.count(last_number_spoken) > 1:

		indices = [i for i, x in enumerate(numbers_spoken) if x == last_number_spoken]
		numbers_spoken.append(indices[-1] - indices[-2])
	else:
		numbers_spoken.append(0)

print numbers_spoken
print numbers_spoken[len(numbers_spoken) - 1]