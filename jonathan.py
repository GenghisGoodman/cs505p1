def display(user, ui):
	#TODO: authentication
	if len(ui) < 2:
		print('>>> USAGE: display <tablename> <<<')
		return

	tablename = ui[1]
	try:
		with open(tablename+'.csv', 'r') as f:
			table = [l.rstrip().split(',') for l in f.readlines()]
	except FileNotFoundError:
		print(">>> ERROR: Table does not exist <<<")
		return
	
	#Get sizes of each input for display
	maxlen = [max([len(i[j]) for i in table])+2 for j in range(len(table[0]))]

	print('='*(sum(maxlen)+3))
	print("#  ", sep='', end='')
	for j in range(len(table[0])):
		print(table[0][j].upper()+(' '*(maxlen[j]-len(table[0][j]))), sep='', end='')
	print()
	print('='*(sum(maxlen)+3))
	for i in range(1,len(table)):
		print(i, end='  ')
		for j in range(len(table[i])):
			print(table[i][j]+(' '*(maxlen[j]-len(table[i][j]))), sep='', end='')
		print()
		
def write(user, ui):
	#TODO: Authentication
	if len(ui) < 3:
		print(">>> USAGE: write <tablename> <entry>")
		return
	
	tablename = ui[1]
	
	try:
		with open(tablename+'.csv', 'r') as f:
			legend = f.readline().rstrip().split(',')
	except FileNotFoundError:
		print(">>> ERROR: Table does not exist")
		return
		
	if len(ui) > 2+len(legend):
		print(">>> ERROR: Too many arguments")
		return		
	
	
	with open(tablename+'.csv', 'a') as f:
		x = ui[2:]
		x += ['NULL']*(len(legend)-len(x))
		f.write("\n"+",".join(x))
		print(">>> Wrote (  ", end='')
		for i in x:
			print(i + "  ", end='')
		print(") to table", tablename)
		
def delete(user, ui):
	#TODO: Authentication
	if len(ui) < 3:
		print(">>> USAGE: delete <tablename> <entryno>")
		return
	
	try:
		with open(ui[1]+'.csv', 'r') as f:
			table = [l.rstrip().split(',') for l in f.readlines()]
		if len(table) <= int(ui[2]) or int(ui[2]) <= 0:
			print(">>> ERROR: Invalid entry number")
		x = table.pop(int(ui[2]))
		with open(ui[1]+'.csv', 'w') as f:
			for i in table[:-1]:
				f.write(",".join(i) + "\n")
			f.write(",".join(table[len(table)-1]))
		print(">>> Deleted (  ", end='')
		for i in x:
			print(i + "  ", end='')
		print(") from table", ui[1])		
		
	except FileNotFoundError:
		print (">>> ERROR: Table does not exist")
		return
	except ValueError:
		print (">>> ERROR: Second argument should be a number")
		return
	