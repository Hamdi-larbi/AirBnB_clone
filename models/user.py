#!/usr/bin/python3

"""class User that inherits from BaseModel:
models/user.py
Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string"""

from models.base_model import BaseModel


class User(BaseModel):
	"""user class"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""
