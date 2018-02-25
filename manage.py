from genghis import create, grant, login, register
from jonathan import display


def main():

	user = ''
	ui = input(user + '>').split(' ')
	
	while ui[0] != 'quit' and ui[0] != 'q':
		
		if ui[0] == 'login':
			user = login(ui)

		if ui[0] == 'register':
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


		
main()
