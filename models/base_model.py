#!/usr/bin/python3

"""  the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
"""

import uuid
from datetime import datetime
import models



class BaseModel():
	""" Base clas model"""
	def __init__(self, *args, **kwargs):
		"""initialise the attributes"""
		if kwargs is None or kwargs == {}:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
		else:
			for key, value in kwargs.items():
				if key == 'created_at':
					self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
				elif key == 'updated_at':
					self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
				else:
					if key != '__class__':
						setattr(self, key, value)

	def __str__(self):
		"""should a readable presentation of BaseModel
		print: [<class name>] (<self.id>) <self.__dict__>"""
		return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
	
	def save(self):
		"""updates the public instance attribute updated_at with the current datetime"""
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__ of the instance"""
		MyDict = {"__class__" : type(self).__name__}
		for key, value in self.__dict__.items():
			if type(value) is datetime:
				MyDict[key] = value.isoformat()
			else:
				MyDict[key] = value
		return MyDict

