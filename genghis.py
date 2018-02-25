from collections import defaultdict

def create(user, ui):
	if len(ui) != 2:
		print('USAGE: CREATE <tablename>')
		return
	with open('grantLog.csv','a') as f:
		f.write(','.join(['admin',user,ui[1],'1','+\n']))

	with open('assigned.csv', 'a') as f:
		f.write('admin,' + ui[1] + ',' +'1' + '\n')
		if user != '':
			f.write(user + ',' + ui[1] + ',' +'1' + '\n')

def grant(user, ui):
	if len(ui) < 5:
		print('USAGE: GRANT <username> <table> <grantOption> <action>')
		return 
	if user == '':
		print('Must be logged in to perform this action!')
		return

	with open('grantLog.csv', 'a') as f:
		f.write(','.join([user] + ui[1:])+'\n')

	try:
		with open('assigned.csv', 'r') as f:
			d = [l.rstrip().split(',') for l in f.readlines()]

		found = False
		for i,l in enumerate(d):
			user, table, b = l
			if user == ui[1] and table == ui[2]:
				d[i] = user,table, str(int(ui[3]) or int(b))
				found = True
		if not found:
			d.append(ui[1:4])

	except FileNotFoundError:
		d = [ui[1:4]]

	with open('assigned.csv', 'w') as f:
		for l in d:
			f.write(','.join(l)+'\n')


def login(ui):
	if len(ui) < 3:
		print('>>> USAGE: login <username> <password>  <<<')
		return ''

	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p in loginTable:
		if ui[1] == u:
			if ui[2] == p:
				return ui[1]
			else:
				print('invalid password')
				return ''

	print('invalid username')
	return ''

def register(ui):
	if len(ui) < 3:
		print('>>> USAGE: register <username> <password>  <<<')
		return ''

	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p in loginTable:
		if u == ui[1]:
			print('ERROR: User already exists')
			return

	with open('login.csv', 'a') as f:
		f.write(','.join(ui[1:])+'\n')

def authenticate(user, fileName, permission):

	usergraph = defaultdict(list)
	with open('grantLog.csv', 'r') as f:
		line = f.readline()
		while line != '':
			u1, u2, fn, b, p = line.rstrip().split(',')
			if fn == fileName and (p == permission or p == '+'):
				usergraph[u1].append([u2, b])
			line = f.readline()

	stack = ['admin']
	seen = defaultdict(int)
	current = ''
	while current != user and len(stack) > 0:
		current = stack.pop()
		for node in usergraph[current]:
			u,b = node 
			if not seen[u] and int(b):
				stack.append(u)

			elif not seen[u]:
				if u == user:
					current = u
					break
		seen[current] = 1

	return current == user






