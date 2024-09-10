import json
from ImageJson import ImageJSON
import unittest


class TestImageJson(unittest.TestCase):
    def test_date_from_json(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_images = json.load(image_input_file)
        first_image = test_images[0]
        first_obj = ImageJSON(first_image)
        self.assertEqual(first_obj.get_date(), "2003-05-16")
        second_image = test_images[1]
        second_obj = ImageJSON(second_image)
        self.assertEqual(second_obj.get_date(), "2003-05-17")
        second_image = test_images[1]
        second_obj = ImageJSON(second_image)
        self.assertNotEqual(second_obj.get_date(), "2004-05-17")
    def test_explanation_from_json(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_images = json.load(image_input_file)
        first_image = test_images[0]
        first_obj = ImageJSON(first_image)
        self.assertEqual(first_obj.get_explanation(), "This colorful telescopic view towards the northern constellation Lyra reveals dim outer regions around M57, popularly known as the Ring Nebula. While modern astronomers still refer to M57 as a planetary nebula, at one light-year across M57 is not a planet but the gaseous shroud of a dying sun-like star. Roughly the same apparent size as M57, the fainter, often overlooked barred spiral galaxy IC1296 is at the lower right and would have been referred to in the early 20th century as a spiral nebula. By chance the pair are in the same field of view, and while they appear to have similar sizes they are actually very far apart. M57 lies at a distance of a mere 2,000 light-years, well within our own Milky Way galaxy. Extragalactic IC1296 is more like 200,000,000 light-years distant or about 100,000 times farther away. Since they appear roughly similar in size, spiral nebula IC1296 must also be about 100,000 times larger than planetary nebula M57.")
        self.assertNotEqual(first_obj.get_explanation(), "The cow jumped over the moon")
    def test_get_image_from_json(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_images = json.load(image_input_file)
        first_image = test_images[0]
        first_obj = ImageJSON(first_image)
        self.assertEqual(first_obj.get_image(), "https://apod.nasa.gov/apod/image/0305/nebulae_lula_full.jpg")
        self.assertNotEqual(first_obj.get_image(), "picture")
    def test_get_type_from_json(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_images = json.load(image_input_file)
        first_image = test_images[0]
        first_obj = ImageJSON(first_image)
        self.assertEqual(first_obj.get_type(), "image")
        self.assertNotEqual(first_obj.get_type(), "picture")
        last_image = test_images[len(test_images)-1]
        last_obj = ImageJSON(last_image)
        self.assertEqual(last_obj.get_type(), "video")
    def test_get_title_from_json(self):
        with open("my_tests_file.json", 'r') as image_input_file:
            test_images = json.load(image_input_file)
        first_image = test_images[0]
        first_obj = ImageJSON(first_image)
        self.assertEqual(first_obj.get_title(), "A Tale of Two Nebulae")
        self.assertNotEqual(first_obj.get_title(), "picture")
        last_image = test_images[len(test_images)-1]
        last_obj = ImageJSON(last_image)
        self.assertEqual(last_obj.get_title(), "The Earth and Moon from Mars")
