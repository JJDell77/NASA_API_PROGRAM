from ImageJson import ImageJSON

class ImageCollection:

    def __init__(self, name, sort=None):
        self.name = name
        self._image_obj_collection = []
        self.sorted_by = sort

    def add_obj(self, obj):
        for i in self._image_obj_collection:
            if obj.get_title() == i.get_title():
                return
        self._image_obj_collection.append(obj)
        self.sorted_by = "Unsorted"

    def get_obj_list(self):
        return self._image_obj_collection

    def get_name(self):
        return self.name

    def rename_collection(self, name):
        self.name = name

    def get_obj(self, title):
        for obj in self._image_obj_collection:
            if obj.get_title() == title:
                return obj
        return "Object not found"

    def sort_by_title(self):
        if self.sorted_by == "title":
            return
        self.sorted_by = "title"
        self._image_obj_collection.sort(key=lambda image_obj: image_obj.get_title())

    def sort_by_date(self):
        if self.sorted_by == "date":
            return
        self.sorted_by = "date"
        self._image_obj_collection.sort(key=lambda image_obj: image_obj.get_date())


