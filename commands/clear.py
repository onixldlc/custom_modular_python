import os

def func(commandsDict,args):
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

cmd = {
	"name":"clear",
	"function":func,
	"help":"clear console"
}