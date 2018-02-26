from collections import defaultdict
import datetime


def forbid(user, ui):
	if user != 'admin':
		print("ERROR: Only admin has access to forbid function")
		return 0
	if len(ui) < 3:
		print("USAGE: forbid <user> <table>")
		return 0

	try:
		with open('forbidden.csv', 'r') as f:
			d =[l.rstrip().split(',') for l in f.readlines()]

		for u,t in d:
			t = t.rstrip()
			if u == ui[1] and t == ui[2]:
				print('ERROR: '+u+' is already forbidden from '+t)
				return 0

		with open('assigned.csv', 'r') as fa:
			da = [l.rstrip().split(',') for l in fa.readlines()]

		remove = []
		for i,l in enumerate(da):
			u,t,b = l
			t = t.rstrip()
			if u == ui[1] and t == ui[2]:
				print('ERROR: '+u+' is assigned to '+t)
				print('Inserting ({U},{T}) into forbidden may result in disruption of operations.'.format(U = u, T = t))
				confirm = input('Are you sure you want to proceed? (y/n)>')
				confirm = confirm == 'y'
				if not confirm:
					return 0
				remove.append(i)
		[da.pop(i) for i in remove]

		with open('assigned.csv', 'w') as fw:
			for l in da:
				fw.write(','.join(l)+'\n')
					
	except FileNotFoundError:
		pass

	with open('forbidden.csv', 'a') as f:
		f.write(','.join(ui[1:])+'\n')

	message = '{date} -- You have been forbidden access to {table} by admin'.format(
				date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
				table = ui[2])

	leaveMessage(ui[1], message)

	return 1

def assign(user, ui):
	if user != 'admin':
		print("ERROR: Only admin has access to forbid function")
		return 0
	if len(ui) < 3:
		print("USAGE: assign <user> <table>")
		return 0
	try:
		with open('assigned.csv', 'r') as f:
			d =[l.rstrip().split(',') for l in f.readlines()]

		for u,t,b in d:
			t = t.rstrip()
			if u == ui[1] and t == ui[2]:
				print('ERROR: '+u+' is already assigned to '+t)
				return 0

		with open('forbidden.csv', 'r') as fa:
			da = [l.rstrip().split(',') for l in fa.readlines()]

		remove = []
		for i,l in enumerate(da):
			u,t = l
			t = t.rstrip()
			if u == ui[1] and t == ui[2]:
				print('ERROR: '+u+' is forbidden from '+t)
				print('Inserting ({U},{T}) into assigned may result in security issues'.format(U = u, T = t))
				confirm = input('Are you sure you want to proceed? (y/n)>')
				confirm = confirm == 'y'
				if not confirm:
					return
				remove.append(i)
		[da.pop(i) for i in remove]

		with open('forbidden.csv', 'w') as fw:
			for l in da:
				fw.write(','.join(l)+'\n')
					
	except FileNotFoundError:
		pass

	with open('assigned.csv', 'a') as f:
		f.write(','.join(ui[1:])+',1\n')

	message = '{date} -- You have been assigned access to {table} by admin'.format(
				date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
				table = ui[2])

	leaveMessage(ui[1], message)

	return 1

def create(user, ui):
	if len(ui) != 2:
		print('USAGE: CREATE <tablename>')
		return 0
	with open('grantLog.csv','a') as f:
		f.write(','.join(['admin',user,ui[1],'1','+\n']))

	with open('assigned.csv', 'a') as f:
		f.write('admin,' + ui[1] + ',' +'1' + '\n')
		if user != '':
			f.write(user + ',' + ui[1] + ',' +'1' + '\n')

	return 1

def grant(user, ui):
	if len(ui) != 5:
		print('USAGE: GRANT <username> <table> <grantOption> <action>')
		return 0
	if user == '':
		print('Must be logged in to perform this action!')
		return 0

	error = False
	with open('forbidden.csv', 'r') as nf:
		l = nf.readline().rstrip().split(',')
		while l != ['']:
			if l[0]==ui[1] and l[1] == ui[2]:
				print('ERROR: {u} is forbidden from {t}'.format(u = ui[1], t= ui[2]))
				leaveMessage('admin', "{date} -- {u1} attempted to grant {u2} access to {table}".format(
					date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
					u1 = user,
					u2 = ui[1],
					table = ui[2]))

				error = True
			l = nf.readline().rstrip().split(',')
	if error:
		return 0

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

	message = '{date} -- You have been granted access to {table} by {gu}'.format(
				date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
				table = ui[2],
				gu = user)

	leaveMessage(ui[1], message)
		
	return 1

def login(ui):
	if len(ui) != 3:
		print('>>> USAGE: login <username> <password>  <<<')
		return ''

	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p,m in loginTable:
		if ui[1] == u:
			if ui[2] == p:
				print('INBOX:',m)
				return ui[1]
			else:
				print('invalid password')
				return ''

	print('invalid username')
	return ''

def register(ui):
	if len(ui) != 3:
		print('>>> USAGE: register <username> <password>  <<<')
		return 0

	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p,m in loginTable:
		if u == ui[1]:
			print('ERROR: User already exists')
			return 0

	with open('login.csv', 'a') as f:
		f.write(','.join(ui[1:])+',Welcome {U}!\n'.format(U = ui[1]))

	return 1

def leaveMessage(receiver, message):
	with open('login.csv','r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for i,l in enumerate(loginTable):
		u,p,m = l
		if u == receiver:
			loginTable[i][2] = message

	with open('login.csv','w') as f:
		for l in loginTable:
			f.write(','.join(l)+'\n')		

def authenticate(user, fileName, permission):

	forbidden = defaultdict(lambda: defaultdict(int))

	with open('forbidden.csv', 'r') as nf:
		l = nf.readline().rstrip().split(',')
		while l != ['']:
			forbidden[l[0]][l[1]] = 1
			l = nf.readline().rstrip().split(',')

	usergraph = defaultdict(list)
	with open('grantLog.csv', 'r') as f:
		line = f.readline()
		while line != '':
			u1, u2, fn, b, p = line.rstrip().split(',')
			if fn == fileName and (p == permission or p == '+') and not forbidden[u2][fn]:
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



