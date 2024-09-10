from ImageCollection import ImageCollection
from ImageJson import ImageJSON
import json
import unittest


def create_example_collection(self):
    with open("my_tests_file.json", 'r') as image_input_file:
        test_obj = json.load(image_input_file)
    first_obj = ImageJSON(test_obj[3])
    second_obj = ImageJSON(test_obj[1])
    third_obj = ImageJSON(test_obj[2])
    fourth_obj = ImageJSON(test_obj[0])
    my_collection = ImageCollection('Deep Space')
    my_collection.add_obj(first_obj)
    my_collection.add_obj(second_obj)
    my_collection.add_obj(third_obj)
    my_collection.add_obj(fourth_obj)
    return my_collection


class TestImageCollection(unittest.TestCase):

    def test_add_obj_and_get_obj(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_obj = json.load(image_input_file)
        first_obj = ImageJSON(test_obj[0])
        second_obj = ImageJSON(test_obj[1])
        third_obj = ImageJSON(test_obj[2])
        my_collection = ImageCollection("my collection")
        my_collection.add_obj(first_obj)
        my_collection.add_obj(second_obj)
        my_collection.add_obj(third_obj)
        self.assertIn(first_obj, my_collection.get_obj_list())
        self.assertIn(second_obj, my_collection.get_obj_list())
        self.assertIn(third_obj, my_collection.get_obj_list())

    def test_get_name(self):
        my_collection = create_example_collection(self)
        self.assertEqual(my_collection.get_name(), "Deep Space")


    def test_rename_collection(self):
        my_collection = create_example_collection(self)
        my_collection.rename_collection("Deep Space")
        self.assertEqual(my_collection.get_name(), "Deep Space")
        my_collection.rename_collection("Milky Way")
        self.assertEqual(my_collection.get_name(), "Milky Way")

    def test_get_obj_list(self):
        my_collection = create_example_collection(self)
        self.assertEqual(my_collection.get_obj_list(), my_collection._image_obj_collection)

    def test_sort_by_title(self):
        my_collection = create_example_collection(self)
        sorted_test = sorted(my_collection._image_obj_collection, key=lambda obj: obj.get_title())
        my_collection.sort_by_title()
        my_list = my_collection.get_obj_list()
        self.assertSequenceEqual(my_list, sorted_test)


    def test_sort_by_date(self):
        my_collection = create_example_collection(self)
        sorted_test = [my_collection._image_obj_collection[3], my_collection._image_obj_collection[1],
                       my_collection._image_obj_collection[2], my_collection._image_obj_collection[0]]
        my_collection.sort_by_date()
        my_list = my_collection.get_obj_list()
        self.assertSequenceEqual(my_list, sorted_test)





