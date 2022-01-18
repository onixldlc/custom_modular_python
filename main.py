import os
import sys
import importlib

exitCommands = ["exit", "quit"]
reloadCommand = ["reload_commands"]


def allCmd(cmdFiles):
	commands = {}

	for file in os.listdir(os.path.dirname(cmdFiles)):
		if file[-3:] == ".py":
			mod_name = file[:-3]   # strip .py at the end
			print(mod_name)

			tmp = importlib.import_module('commands.'+mod_name).cmd
			# print(tmp,cmdFiles+mod_name)
			commands[tmp["name"].lower()] = {"function":tmp["function"],"help":tmp["help"]}
	
	return commands




def executeCommand(commandsDict,text,args):
	command = commandsDict.get(text).get("function")
	try:
		command(commandsDict,args)
	except:
		print(f"there is no command such as: {text}")
		pass



def main():
	commands = allCmd("./commands/")

	# print(commands)

	while(True):
		cmdInput = input().lower().split(" ")
		cmd = cmdInput[0]
		args = []
		
		if len(args) > 1:
			args = cmdInput[1:]

		if cmd in exitCommands:
			break
		else:
			executeCommand(commands,cmd,args)
		
	print("order 66 executed !!!")

if __name__ == "__main__" :
	main()








# print(sys.path)
# sys.path.append("/commands")
# print(f"Name: {__name__}")
# print(f"Package: {__package__}")
# from commands.test import cmd
# print(cmd)
# commands = allCmd("./pythonUtils/commands/")
# exitCommands = ["exit", "quit"]
# executeCommand(commands,"tes")

# print(commands)

# while(True):
# 	cmdInput = input().lower().split(" ")
# 	cmd = cmdInput[0]
# 	args = []
	
# 	if len(args) > 1:
# 		args = cmdInput[1:]

# 	if cmd in exitCommands:
# 		break
# 	else:
# 		executeCommand(commands,cmd,args)
	
# print("order 66 executed !!!")