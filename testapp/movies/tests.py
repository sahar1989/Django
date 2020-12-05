from django.test import TestCase
from movies.api import MovieAPI as api
# Create your tests here.
""" Unit tests:
        Verify functional behavior of individual components, often to class and function level. """
    
class MovieAPITestClass(TestCase):
    
    film={}
    people={}
    
    @classmethod
    def setUpTestData(self):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        self.film = {
              "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
              "title": "Castle in the Sky",
              "description": "The orphan Sheeta inherited a mysterious crystal ...",
              "director": "Hayao Miyazaki",
              "producer": "Isao Takahata",
              "release_date": "1986",
              "rt_score": "95",
              "people": [
                "https://ghibliapi.herokuapp.com/people/"
              ],
              "species": [
                "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
              ],
              "locations": [
                "https://ghibliapi.herokuapp.com/locations/"
              ],
              "vehicles": [
                "https://ghibliapi.herokuapp.com/vehicles/"
              ],
              "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe",
            }

        self.people = {
              "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
              "name": "Pazu",
              "gender": "Male",
              "age": "13",
              "eye_color": "Black",
              "hair_color": "Brown",
              "films": [
                "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
              ],
              "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
              "url": "https://ghibliapi.herokuapp.com/people/fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
            }
        pass
          
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass
        
    def test_something_that_will_pass(self):
        print("test_something_that_will_pass")
        
    def test_something_that_will_fail(self):
        print("test_something_that_will_fail")
        
    def test_parse_films(self):
        print("Method: test_parse_films")
        expected = {
            'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe',
            'title': 'Castle in the Sky',
            'people':[],
        }
        self.assertEqual(api.parse_films(self.film), expected)    
  
    def test_extract_id_from_url(self):   
        print("Method: test_extract_id_from_url")
        expected = ["2baf70d1-42bb-4437-b551-e5fed5a87abe"] 
        self.assertEqual([api.extract_id_from_url(film) 
                for film in self.people.get('films')], expected)   
   
    def test_parse_people(self):
        print("Method: test_parse_people")
        expected = {
            'name': 'Pazu',
            'films_id': ['2baf70d1-42bb-4437-b551-e5fed5a87abe']
        }
        self.assertEqual(api.parse_people(self.people), expected)         