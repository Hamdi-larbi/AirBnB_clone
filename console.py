#!/usr/bin/python3


"""A console to create data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models



class HBNBCommand(cmd.Cmd):
	"""a consule to manage data"""

	prompt = '(hbnb)'

	__class_dict = {"BaseModel": BaseModel,
			"User": User,
			"State": State,
			"City": City,
			"Amenity": Amenity,
			"Place": Place,
			"Review": Review}

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
		"""create <class_name> : Creates a new instance of BaseModel"""
		if class_name == "":
			print("** class name missing **")
		elif class_name not in HBNBCommand.__class_dict:
			print("** class doesn't exist **")
		else:
			#obj = eval(class_name + "()")
			obj = HBNBCommand.__class_dict[class_name]()
			models.storage.save()
			print(obj.id)

	def do_show(self, line):
		"""show <class_name> <class_id> : Prints the string representation
		of an instance based on the class name and id"""
		arg = line.split()
		if len(arg) == 0:
			print("** class name missing **")
		elif arg[0] not in  HBNBCommand.__class_dict:
			print("** class doesn't exist **")
		elif len(arg) == 1:
			print("** instance id missing **")
		else:
			key = "{}.{}".format(arg[0], arg[1])
			if key not in models.storage.all():
				print("** no instance found **")
			else: 
				print(models.storage.all()[key])

	def do_destroy(self, line):
		"""destroy <class_name> <class_id> : Deletes an instance based on the class name and id"""
		arg = line.split()
		if len(arg) == 0:
			print("** class name missing **")
		elif arg[0] not in HBNBCommand.__class_dict:
			print("** class doesn't exist **")
		elif len(arg) == 1:
			print("** instance id missing **")
		else:
			key = "{}.{}".format(arg[0], arg[1])
			if key not in models.storage.all():
				print("** no instance found **")
			else:
				del models.storage.all()[key]
				models.storage.save()

	def do_all(self,line):
		"""all [class_name] :  Prints all string representation
		of all instances based or not on the class name"""
		if line:
			if line in HBNBCommand.__class_dict:
				instance_list = []
				for key, value in models.storage.all().items():
					arg = key.split('.')
					if arg[0] == line:
						instance_list.append(str(value))
				print(instance_list)
			else:
				print("** class doesn't exist **")
		else:
			instance_list = [str(value) for value in models.storage.all().values()]
			print(instance_list)

	def do_update(self, line):
		"""update <class name> <id> <attribute name> "<attribute value>" : Updates an instance
		based on the class name and id by adding or updating attribute"""
		arg = line.split()
		if not line:
			print("** class name missing **")
		else:
			if arg[0] not in HBNBCommand.__class_dict:
				print("** class doesn't exist **")
			elif len(arg) < 2:
				print("** instance id missing **")
			else:
				key = "{}.{}".format(arg[0], arg[1])
				if key not in models.storage.all():
					print("** no instance found **")
				elif len(arg) < 3:
					print("** attribute name missing **")
				elif len(arg) < 4:
					print("** value missing **")
				else:
					arg = arg[:4]
					obj = models.storage.all()[key]
					if arg[2] in obj.__dict__:
						att_type = type(obj.__dict__[arg[2]])
						arg[3] = att_type(arg[3])
					setattr(obj, arg[2], arg[3])
					models.storage.save()



if __name__ == '__main__':
	HBNBCommand().cmdloop()
