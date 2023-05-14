#!/usr/bin/python3

""" a class FileStorage that serializes instances to a JSON file
 and deserializes JSON file to instances"""

import json
import os
from models.base_model import BaseModel


#class_dict = {
#    "BaseModel": BaseModel,
#    "User": User,
#    "Place": Place,
#    "Amenity": Amenity,
#    "City": City,
#    "Review": Review,
#    "State": State
#}

class FileStorage():
	"""FileStorage class"""
	__file_path = 'file.json'
	__objects = {}

	def all(self):
		"""returns the dictionary __objects"""
		return FileStorage.__objects

	def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		with open(FileStorage.__file_path, "w", encoding = "utf-8") as f:
			mydict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
			json.dump(mydict, f)

	def reload(self):
		""" deserializes the JSON file to __objects
		only if the JSON file (__file_path) exists ; otherwise, do nothing"""
		if os.path.exists(FileStorage.__file_path) is False:
			return
		else:
			with open(FileStorage.__file_path, "r", encoding = "utf-8") as f:
				mydict = json.load(f)
				for key, value in mydict.items():
					obj = eval(value["__class__"])(**value)
					FileStorage.__objects[key] = obj


