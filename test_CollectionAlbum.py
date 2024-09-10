from CollectionAlbum import CollectionAlbum
from ImageCollection import ImageCollection
from ImageJson import ImageJSON
import json
import unittest

def create_example_album(self, name=None):
    with open("my_tests_file.json", 'r') as image_input_file:
        test_obj = json.load(image_input_file)
    first_obj = ImageJSON(test_obj[3])
    second_obj = ImageJSON(test_obj[1])
    third_obj = ImageJSON(test_obj[2])
    fourth_obj = ImageJSON(test_obj[0])
    my_collection = ImageCollection("my collection")
    my_collection.add_obj(first_obj)
    my_collection.add_obj(second_obj)
    my_collection.add_obj(third_obj)
    my_collection.add_obj(fourth_obj)
    my_album = CollectionAlbum()
    my_album.add(my_collection)
    return my_album



class TestCollectionAlbum(unittest.TestCase):

    def test_get_collection(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_obj = json.load(image_input_file)
        first_obj = ImageJSON(test_obj[3])
        second_obj = ImageJSON(test_obj[1])
        third_obj = ImageJSON(test_obj[2])
        fourth_obj = ImageJSON(test_obj[0])
        name = "my collection"
        my_collection = ImageCollection(name)
        my_collection.add_obj(first_obj)
        my_collection.add_obj(second_obj)
        my_collection.add_obj(third_obj)
        my_collection.add_obj(fourth_obj)
        my_album = CollectionAlbum()
        my_album.add(my_collection)
        self.assertEqual(my_album.get_collection("my collection"), my_collection)

    def test_add(self):
        my_album = create_example_album(self)
        my_collection = ImageCollection('name')
        my_album.add(my_collection)
        self.assertIn(my_collection, my_album.image_collections)


    def test_get_list_of_names(self):
        my_album = create_example_album(self)
        test_list = ['my collection']
        self.assertEqual(my_album.get_list_of_names(), test_list)


    def test_rename_collection(self):
        my_album = create_example_album(self)
        new_name = "new name"
        my_album.rename_collection(my_album.image_collections[0], new_name)
        test_list = ['new name']
        self.assertEqual(my_album.get_list_of_names(), test_list)




