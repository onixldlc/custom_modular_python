def func(commandsDict,args):
	print("commands:")
	print("")
	for x in commandsDict:
		print(f"  {x}:")
		print(f"    {commandsDict.get(x).get('help')}")
		print("")

cmd = {
	"name":"list",
	"function":func,
	"help":"this is the command list function"
}