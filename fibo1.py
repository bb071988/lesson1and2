list = [0,1]

stop_value = 10
counter = 0

while counter  < stop_value:
	f = list[counter] + list[counter + 1]
	list.append(f)
	print(f)
	counter += 1