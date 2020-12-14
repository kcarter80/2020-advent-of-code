#busses = [7,13,'x','x',59,'x',31,19]
#busses = [17,'x',13,19]
#busses = [67,7,59,61]
#busses = [67,'x',7,59,61]
#busses = [67,7,'x',59,61]
#busses = [1789,37,47,1889] # 1202161486

busses = [29,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',631,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',13,19,'x','x','x',23,'x','x','x','x','x','x','x',383,'x','x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x',17]

print busses

# this is the first possible time that the first could leave and work 
goal_depart_time = 0
so_far_so_good = False
offset = 1
increment = busses[0]
busses.pop(0)

first_winner_time = None
#print goal_depart_time
while len(busses) > 0:

	print increment, goal_depart_time, busses[0], offset
	if busses[0] == 'x':
		busses.pop(0)
		offset += 1
	else:
		if not (goal_depart_time + offset) % busses[0] == 0:
			goal_depart_time += increment
		else:
			# first winner
			if first_winner_time == None:
				first_winner_time = goal_depart_time
				print 'first winner', first_winner_time
				if len(busses) == 1:
					break
				goal_depart_time += increment

			# second winner
			else:
				busses.pop(0)
				offset += 1
				increment = goal_depart_time - first_winner_time
				first_winner_time = None
				print 'second winner new increment', increment, goal_depart_time
print goal_depart_time