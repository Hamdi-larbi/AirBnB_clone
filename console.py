#!/usr/bin/python3


"""A console to create data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
	"""a consule to manage data"""

	prompt = '(hbnb)'

	def do_EOF(self, line):
		"""EOF to exit the program"""
		print("")
		return True

	def do_quit(self, line):
		"""quit to exit the program"""
		return True

	def emptyline(self):
		"""an empty line + ENTER shouldn t execute anything"""
		pass
	def do_create(self, class_name):
		"""create BaseModel : Creates a new instance of BaseModel"""
		if class_name == "":
			print("** class name missing **")
		elif class_name != "BaseModel":
			print("** class doesn't exist **")
		else:
			obj = class_name()
			print(obj.id)


if __name__ == '__main__':
	HBNBCommand().cmdloop()
