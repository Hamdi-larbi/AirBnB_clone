#!/usr/bin/env python3

"""test cases using unittest"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

	def test_ISinstance(self):
		"""test if object is an ainstance of te BaseModel class"""
		b = BaseModel()
		self.assertIsInstance(b, BaseModel)

	def test_unique_id(self):
		"""Test that every instance id is unique"""
		b1 = BaseModel()
		b2 = BaseModel()
		self.assertNotEqual(b1.id, b2.id)

	def test_type_id(self):
		"""test that the type of the attribute id is str"""
		b = BaseModel()
		self.assertEqual(type(b.id), str)

	def test_type_created_at(self):
		"""test that the type of the attribute created_at is datetime"""
		b = BaseModel()
		self.assertIsInstance(b.created_at, datetime)

	def test_type_updated_at(self):
		"""test that the type of the attribute created_at is datetime"""
		b = BaseModel()
		self.assertIsInstance(b.updated_at, datetime)

	def test_instantiation_with_args_and_kwargs(self):
        	dt = datetime.today()
        	dt_iso = dt.isoformat()
        	b1 = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        	self.assertEqual(b1.id, "345")
        	self.assertEqual(b1.created_at, dt)
        	self.assertEqual(b1.updated_at, dt)






if __name__ == '__main__':
	unittest.main()
