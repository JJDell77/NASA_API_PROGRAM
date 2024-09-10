import json
import requests



class ImageJSON:

    def __init__(self, image_json):
        self._date = image_json['date']
        self._explanation = image_json['explanation']
        self._image = image_json['hdurl']
        self._type = image_json['media_type']
        self._title = image_json['title']

    def __str__(self):
        """prints object"""
        print("Title:", self._title, "\n Date:", self._date, "\n Type:", self._type, "\n Explanation:",
              self._explanation, "\n Image:", self._image)

    def get_date(self):
        date = self._date
        return date

    def get_explanation(self):
        explanation = self._explanation
        return explanation

    def get_image(self):
        image = self._image
        return image

    def get_type(self):
        type = self._type
        return type

    def get_title(self):
        title = self._title
        return title



def main():
    url = 'https://api.nasa.gov/planetary/apod?api_key=bYgUJCu6QjKcvu7WSAElha7ZFNzZq3Dibeq9vYMV&date=2003-05-16'
    response = requests.get(url)
    data = json.loads(response.text)
    apod = ImageJSON(data)
    title = apod.get_title()
    date = apod.get_date()
    explanation = apod.get_explanation()
    image_url = apod.get_image()
    type_data = apod.get_type()
    print("Title:", title)
    print("Date:", date)
    print("Explanation:", explanation)
    print("Image URL:", image_url)
    print("Type of data:", type_data)


if __name__ == '__main__':
    main()
