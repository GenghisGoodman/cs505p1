



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


def grant():
	pass

		
main()
