#!/usr/bin/python3

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
		b2 = BaseModl()
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

	def test_created_equal_updated(self):
		"""test that created_at is equal to updated_at before update of instance"""
		b = BaseModel()
		self.assertEqual(b.created_at, b.updated_at)





if __name__ == '__main__':
	unittest.main()
