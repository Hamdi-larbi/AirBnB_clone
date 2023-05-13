#!/usr/bin/python3


"""A console to create data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)"""

import cmd


class HBNBCommand(cmd.Cmd):
"""a consule to manage data"""

	prompt = (hbnb)

	def do_EOF(self, line)
	"""EOF to exit the program"""
		return True

	def do_quit(self, line)
	"""quit to exit the program"""
		return True

	def emptyline(self)
	"""an empty line + ENTER shouldn t execute anything"""
		pass




if __name__ == '__main__':
	HBNBCommand().cmdloop()
