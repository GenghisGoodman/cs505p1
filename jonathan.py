from genghis import authenticate

def display(user, ui):
	if len(ui) < 2:
		print('>>> USAGE: display <tablename> <<<')
		return

	tablename = ui[1]
	try:
		with open(tablename+'.csv', 'r') as f:
			table = [l.rstrip().split(',') for l in f.readlines()]
	except FileNotFoundError:
		print(">>> ERROR: Table does not exist <<<")
		return
	
	if not authenticate(user, tablename, 'r'):
		print('>>> ERROR: User', user, 'does not have read access to ', tablename)
		return	
	
	#Get sizes of each input for display
	maxlen = [max([len(i[j]) for i in table])+2 for j in range(len(table[0]))]

	print('='*(sum(maxlen)+3))
	print("#  ", sep='', end='')
	for j in range(len(table[0])):
		print(table[0][j].upper()+(' '*(maxlen[j]-len(table[0][j]))), sep='', end='')
	print()
	print('='*(sum(maxlen)+3))
	for i in range(1,len(table)):
		print(i, end='  ')
		for j in range(len(table[i])):
			print(table[i][j]+(' '*(maxlen[j]-len(table[i][j]))), sep='', end='')
		print()
		
def write(user, ui):
	if len(ui) < 3:
		print(">>> USAGE: write <tablename> <entry>")
		return
	
	tablename = ui[1]
	
	try:
		with open(tablename+'.csv', 'r') as f:
			legend = f.readline().rstrip().split(',')
	except FileNotFoundError:
		print(">>> ERROR: Table does not exist")
		return
	
	if not authenticate(user, tablename, 'w'):
			print('>>> ERROR: User', user, 'does not have write access to ', tablename)
			return		
	
	if len(ui) > 2+len(legend):
		print(">>> ERROR: Too many arguments")
		return		
	
	
	with open(tablename+'.csv', 'a') as f:
		x = ui[2:]
		x += ['NULL']*(len(legend)-len(x))
		f.write("\n"+",".join(x))
		print(">>> Wrote (  ", end='')
		for i in x:
			print(i + "  ", end='')
		print(") to table", tablename)
		
def delete(user, ui):
	if len(ui) < 3:
		print(">>> USAGE: delete <tablename> <entryno>")
		return
	
	try:
		with open(ui[1]+'.csv', 'r') as f:
			table = [l.rstrip().split(',') for l in f.readlines()]
	except FileNotFoundError:
		print (">>> ERROR: Table does not exist")
		return	
	
	if not authenticate(user, tablename, 'r'):
			print('>>> ERROR: User', user, 'does not have write access to', tablename)
			return
		
	try:
		if len(table) <= int(ui[2]) or int(ui[2]) <= 0:
			print(">>> ERROR: Invalid entry number")
			return
		x = table.pop(int(ui[2]))
	except ValueError:
		print (">>> ERROR: Second argument should be a number")
		return	
	
	with open(ui[1]+'.csv', 'w') as f:
		for i in table[:-1]:
			f.write(",".join(i) + "\n")
		f.write(",".join(table[len(table)-1]))
	print(">>> Deleted (  ", end='')
	for i in x:
		print(i + "  ", end='')
	print(") from table", ui[1])		
	

def Help(user, ui):
	if len(ui) == 1:
		print ("cs505p1 by Genghis Goodman and Jonathan Dingess.",
		       "This is a database system implementing a mixture of DAC and MAC.",
		       "To be specific, GRANT options of DAC are implemented together with a chief security officer (SO) to oversee.",
		       "",
		       "Usable commands:",
		       "\tlogin <user> <password>\t\t\t\t\tLogs in to the user account.",
		       "\tregister <user> <password>\t\t\t\tRegisters a new account.",
		       "\tcreate <tablename>\t\t\t\t\tCreate a table with the given name.",
		       "\tdisplay <tablename>\t\t\t\t\tDisplay the contents of the given table.", 
		       "\twrite <tablename> <entry>\t\t\t\tWrite the given entry to the given table.",
		       "\tdelete <tablename> <entryno>\t\t\t\tDelete the numbered entry from the given table.", 
		       "\tgrant <user> <tablename> <grantOption> <action>\t\tGrant the user permission to do action on table.",
		       "\thelp <command>\t\t\t\t\t\tShow this dialog, or show specific information about a certain command.", sep='\n')
		if (user == 'admin'):
			print("",
			      "Admin-only commands:",
			      "\tforbid <user> <tablename>\t\t\t\tAdmin only: Forbid a user from performing an action on a table.", sep="\n")
	else:
		if ui[1] == "login":
			print("login <user> <password>",
			      "",
			      "Log in to the user account with the username and password.",
			      "If password is not correct nothing will happen.",
			      "If you have forgotten your username or password, contact your security officer (SO)", sep='\n')
		if ui[1] == "register":
			print("register <user> <password>",
			      "",
			      "Register a new account with the username and password.",
			      "This does not change current user; you must still log in to the new account.",
			      "New accounts do not inherit permissions; you must grant permissions to them.", sep="\n")
		if ui[1] == "create":
			print("create <tablename>",
			      "",
			      "Create a new table with the given tablename.",
			      "The currently logged in user has all access rights to the table they create."
			      "No other user (Besides admin) has access, so the owner must grant others permission.", sep="\n")
		if ui[1] == "display":
			print("display <tablename>",
			      "",
			      "Display the contents of a table.",
			      "The logged-in user must have read access to the table to use this command.", sep="\n")
		if ui[1] == "write":
			print("write <table> <entry>",
			      "",
			      "Write an entry to the end of table.",
			      "The entry field can consist of one or more arguments. Any spaces left blank in the table will be left NULL."
			      "The logged-in user must have write access to the table to use this command.", sep="\n")
		if ui[1] == "delete":
			print("delete <tablename> <entryno>",
			      "",
			      "Delete an entry from a table.",
			      "entryno should be the number of the entry you wish to delete, corresponding to the leftmost number in the display command.",
			      "The logged-in user must have write access to the table to use this command.", sep="\n")
		if ui[1] == "grant":
			print("grant <user> <tablename> <grantOption> <action>",
			      "",
			      "Grant user permission to perform action on a table, and optionally grant them the ability to grant to others as well.",
			      "grantOption should be 1 or 0, if you want the user to be able to grant to others or not.",
			      "action should be 'r', 'w', or '+', to give the user access to read, write, or both read and write.", sep="\n")
		if ui[1] == "help":
			print("You need help using the help function?")
		if ui[1] == "forbid" and user == "admin":
			print("forbid <user> <tablename>",
			      "",
			      "Admin-only command.", 
			      "Forbid a user from performing any action on the given table.",
			      "The user will not be able to access the table at all, even if others grant him access, until they are removed from the forbidden list.", sep="\n")
		