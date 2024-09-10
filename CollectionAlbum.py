
from ImageCollection import ImageCollection


class CollectionAlbum:

    def __init__(self):
        self.image_collections = []
        self.list_of_names = []

    def add(self, collection):
        self.image_collections.append(collection)
        self.list_of_names.append(collection.get_name())

    def get_collection(self, name):
        for collection in self.image_collections:
            if collection.get_name() == name:
                return collection
        return "Collection not found"

    def get_list_of_names(self):
        return self.list_of_names

    def rename_collection(self, collection, new_name):
        place = self.image_collections.index(collection)
        self.list_of_names[place] = new_name
        collection.rename_collection(new_name)
