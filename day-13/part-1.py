earliest_timestamp_could_depart = 939
busses = [7,13,'x','x',59,'x',31,19]

earliest_timestamp_could_depart = 1000507
busses = [29,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',631,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',13,19,'x','x','x',23,'x','x','x','x','x','x','x',383,'x','x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x',17]

earliest_bus = None
earliest_time = None
for bus in busses:
	if bus != 'x':
		i = 0
		while i * bus < earliest_timestamp_could_depart:
			i += 1
		if earliest_time == None or i * bus < earliest_time:
			earliest_time = i * bus
			earliest_bus = bus

print earliest_time
print earliest_bus

print (earliest_time - earliest_timestamp_could_depart) * earliest_bus