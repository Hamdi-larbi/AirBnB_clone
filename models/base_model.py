#!/usr/bin/python3

"""  the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
"""

import uuid
from datetime import datetime



class BaseModel():
""" Base clas model"""
	def __init__(self):
	"""initialise the attributes"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
	"""should a readable presentation of BaseModel
	print: [<class name>] (<self.id>) <self.__dict__>"""
		return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
	
	def save(self):
	"""updates the public instance attribute updated_at with the current datetime"""
		self.updated_at = datetime.now()

	def to_dict(self):
	"""returns a dictionary containing all keys/values of __dict__ of the instance"""
		MyDict = {"__class__" : type(self).__name__}
		for key, value in self__dic__.items:
			if type(value) is datetime:
				MyDict[key] = value.isoformat()
			else:
				MyDict[key] = value
		return MyDict

