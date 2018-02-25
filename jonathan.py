def display(user, ui):
	if len(ui) < 2:
		print('>>> USAGE: display <tablename> <<<')
		return

	tablename = ui[1]
	with open(tablename+'.csv', 'r') as f:
		table = [l.rstrip().split(',') for l in f.readlines()]
	
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