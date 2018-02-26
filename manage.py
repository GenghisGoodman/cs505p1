from genghis import create, grant, login, register, forbid
from jonathan import display, write, delete, Help


def main():

	user = ''
	ui = input(user + '>').split(' ')
	
	while ui[0] != 'quit' and ui[0] != 'q':
		
		if ui[0].lower() == 'login':
			user = login(ui)

		if ui[0].lower() == 'register':
			register(ui)
					
		if ui[0].lower() == 'display':
			display(user, ui)

		if ui[0].lower() == 'create':
			create(user, ui)

		if ui[0].lower() == 'grant':
			grant(user, ui)

		if ui[0].lower() == 'help':
			Help(user, ui)

		if ui[0].lower() == 'write':
			write(user, ui)
			
		if ui[0].lower() == 'delete':
			delete(user, ui)

		if ui[0].lower() == 'forbid':
			forbid(user, ui)


		ui = input(user + '>').split(' ')


		
main()
