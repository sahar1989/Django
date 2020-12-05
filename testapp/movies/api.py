import requests

class MovieAPI:
    """ global variables """
    base_url = 'https://ghibliapi.herokuapp.com/'
    FILMS='films'
    PEOPLE='people'
    
    @classmethod
    def parse_films(self, film):
        """ extract id, title and create people object field to be fill later """
        return {
            'id': film.get('id'),
            'title': film.get('title'),
            'people':[],
        }
        
    @classmethod    
    def extract_id_from_url(self, film):
        """ film id is a url then just extract the id exp: https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6 """
        return film.split('/')[-1]
        
    @classmethod    
    def parse_people(self, people):
        """extract name, films from people"""
        return {
            'name': people.get('name'),
            'films_id': [
                self.extract_id_from_url(film) 
                for film in people.get('films')
            ],

        }
        
    @classmethod    
    def get_movie_data(self):
        
        """ get films date from url api """ 
        films_data = requests.get(self.base_url+self.FILMS).json()

        """ get people data from url api """
        people_data = requests.get(self.base_url+self.PEOPLE).json()

        films = [self.parse_films(film) for film in films_data]
        people = [self.parse_people(p) for p in people_data]
                    
        final_data = films.copy() 

        """ bind people and film """
        for p in people:
            for p_film_id in p['films_id']:   
                for film in final_data:
                    if p_film_id == film['id']:
                        film['people'].append(p['name'])
            
              
        """ return data to template """           
        return final_data

