import os
import sys
import importlib
import readline

exitCommands = {
	"exit":{
		"function":0,
		"help":"exit the program"
	},
	"quit":{
		"function":0,
		"help":"exit the program"
	}
}
reloadCommand = {
	"reload":{
		"function":0,
		"help":"reload all the command in the list"
	}
}

dir = "./commands/"

mainCommands = {
	**exitCommands,
	**reloadCommand
}
histfile = os.path.join("./", ".python_cmd_history")


def init():
	try:
		readline.read_history_file(histfile)
		readline.set_history_length(1024)
	except FileNotFoundError:
		pass

def save_history():
	readline.write_history_file(histfile)

def allCmd(cmdFiles,flag="load"):
	commands = {**mainCommands}

	for file in os.listdir(os.path.dirname(cmdFiles)):
		if file[-3:] == ".py":
			mod_name = file[:-3]   # strip .py at the end
			# print(mod_name)
			
			yetLoaded = sys.modules.get("commands."+mod_name)
			if(not yetLoaded):
				flag = "load"

			if flag == "load":
				if mod_name in commands:
					print(f"skipping {mod_name} since there is already a command with the same name !!!")
					pass
				tmp = importlib.import_module('commands.'+mod_name).cmd

			elif flag == "reload":
				tmp = importlib.reload(sys.modules.get('commands.'+mod_name)).cmd

			commands[tmp["name"].lower()] = {"function":tmp["function"],"help":tmp["help"]}
	
	return commands


def executeCommand(commandsDict,text,args):
	try:
		command = commandsDict.get(text).get("function")
		command(commandsDict,args)
	except:
		print(f"there is no command such as: {text}")
		pass



def main():
	commands = allCmd(dir)
	init()
	# print(commands)

	while(True):
		cmdInput = input(">>>").lower().split(" ")
		cmd = cmdInput[0]
		args = []
		
		if len(args) > 1:
			args = cmdInput[1:]

		if cmd in exitCommands:
			break
		elif cmd in reloadCommand:
			commands = allCmd(dir,"reload")
		else:
			executeCommand(commands,cmd,args)

	save_history()
	print("yes my lord !!!")

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