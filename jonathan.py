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

	print('='*sum(maxlen))
	for j in range(len(table[0])):
		print(table[0][j]+(' '*(maxlen[j]-len(table[0][j]))), sep='', end='')
	print()
	print('='*sum(maxlen))
	for i in range(1,len(table)):
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
		