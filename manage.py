


def main():

	user = ''
	ui = input(user + '>').split(' ')
	
	while ui[0] != 'quit' and ui[0] != 'q':
		
		if ui[0] == 'login':
			user = login(ui)

		if u[0] == 'register':
			register(ui)
					
		if ui[0] == 'display':
			display(user, ui)

		if ui[0].lower() == 'create':
			create(user, ui)

		if ui[0].lower() == 'grant':
			grant(user, ui)

		if ui[0].lower() == 'help':
			Help()

		if ui[0].lower() == 'write':
			write()


		ui = input(user + '>').split(' ')



def create(user, ui):
	if len(ui) != 2:
		print('USAGE: CREATE <tablename>')

	with open('assigned.csv', 'a') as f:
		f.write('admin' + ',' + ui[1] + ',' +'1' + '\n')
		if user != '':
			f.write(user + ',' + ui[1] + ',' +'1' + '\n')

def grant(user, ui):
	if len(ui) < 3:
		print('USAGE: GRANT <username> <table>')
		return ''

	with open('assigned.csv', 'r') as f:
		d = [l.rstrip().split(',') for l in f.readlines()]

	for i,l in d:
		user, table, b = l
		if user == ui[1] and table == ui[2]:
			d[i] = user,table, ui[3]


def login(ui):
	if len(ui) < 3:
		print('>>> USAGE: login <username> <password>  <<<')
		return ''

	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p in loginTable:
		if username == u:
			if password == p:
				return ui[0]
			else:
				print('invalid password')
				return ''

	print('invalid username')
	return ''


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

		
main()
