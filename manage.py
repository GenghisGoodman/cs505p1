



def main():



	user = ''
	ui = input(user + '>').split(' ')
	
	while ui[0] != 'quit' and ui[0] != 'q':
		
		if ui[0] == 'login':
			if len(ui) < 3:
				print('>>> USAGE: login <username> <password>  <<<')
			else:
				if login(ui[1], ui[2]):
					user = ui[1]
				else:
					print('invalid username or password')
					
		if ui[0] == 'display':
			if len(ui) < 2:
				print('>>> USAGE: display <tablename> <<<')
			else:
				display(ui[1])



		ui = input(user + '>').split(' ')


def login(username, password):
	with open('login.csv', 'r') as f:
		loginTable = [l.rstrip().split(',') for l in f.readlines()]

	for u,p in loginTable:
		if username == u:
			if password == p:
				return True
			else:
				return False

	return False 

def display(tablename):
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
		

def grant():
	pass

		
main()
