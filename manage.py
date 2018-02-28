from security_methods import login, grant, register, forbid, revoke, allow
from table_methods import create, display, write, delete, Help, remove
from collections import defaultdict

def unknownCommand(user, ui):
	print('>>> Unknown command <<<')

def blank(user, ui):
	pass

def main():

	methods = defaultdict(lambda: unknownCommand, [
		('register', register),
		('display', display),
		('create', create),
		('grant', grant),
		('help', Help),
		('write', write),
		('remove', remove),
		('forbid', forbid),
		('delete', delete),
		('revoke', revoke),
		('allow', allow),
		('',blank)
		])

	user = ''
	ui = input(user + '>').split(' ')
	
	while ui[0] != 'quit' and ui[0] != 'q':
		
		if ui[0].lower() == 'login':
			user = login(user, ui)
		else:
			methods[ui[0].lower()](user, ui)

		ui = input(user + '>').split(' ')

		
main()
