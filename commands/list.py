def func(commandsDict,args):
	print("commands:")
	for x in commandsDict:
		print("\t{x}:")
		print("\t\t{x.get('help')}:")

cmd = {
	"name":"list",
	"function":func,
	"help":"this is the command list function"
}