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

class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_one_save(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        self.assertLess(first_updated_at, b1.updated_at)

    def test_two_saves(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        second_updated_at = b1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        b1.save()
        self.assertLess(second_updated_at, b1.updated_at)

    def test_save_with_arg(self):
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.save(None)

class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def test_className_present(self):
        """Test className present"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertNotEqual(dic, b1.__dict__)

    def test_attribute_ISO_format(self):
        """Test datetime field isoformated"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_to_dict_type(self):
        b1 = BaseModel()
        self.assertTrue(dict, type(b1.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        b1 = BaseModel()
        self.assertIn("id", b1.to_dict())
        self.assertIn("created_at", b1.to_dict())
        self.assertIn("updated_at", b1.to_dict())
        self.assertIn("__class__", b1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 98
        self.assertIn("name", b1.to_dict())
        self.assertIn("my_number", b1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertEqual(str, type(b1_dict["created_at"]))
        self.assertEqual(str, type(b1_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        b1 = BaseModel()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(b1.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        b1 = BaseModel()
        self.assertNotEqual(b1.to_dict(), b1.__dict__)

    def test_to_dict_with_arg(self):
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.to_dict(None)




if __name__ == '__main__':
	unittest.main()
