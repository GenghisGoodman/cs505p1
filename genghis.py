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