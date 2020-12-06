## Technologies
#### Simple Python/Django web application developed by, Python, Django load movies list from Studio Ghibli API.
#### Display movie list include film title and people names
#### Cache the view’s response and refresh it every 60 second (1 minute)
#### Unittest for the api, and local url and template

 ### Directory testapp
 #### testapp 
      | _init_.py      
      | asgi.py        
      | settings.py     ---> add app name, cache setting and cache TTL 
      | urls.py         ---> add path movies/ 
      | wsgi.py
 #### movies
     | templates         
         | movies       ---> add index.html 
     | _init_.py
     | admin.py
     | api.py           ---> send requests to get film and people data then parse 
                             to get desired data list of movies with people name 
     | apps.py
     | models.py
     | tests.py         ---> add unit test for functions, url and template   
     | urls.py          ---> add view template path to display index.html
     | views.py         ---> call api, get data and send result to template
     
#### Requirments
     pip install Django
     pip install Requests
     pip install python-memcached 
#### How to run
     cmd cd project folder ---> python manage.py migrate (optional if you want to apply default database)
     cmd cd project folder ---> python manage.py runserver 
     open the browser type ---> 127.0.0.1:8000/movies/ 
#### How to run test
     cmd cd project folder ---> python manage.py test
#### future improvment
* Complete test   
  * using selenium webdriver to simulate user interactivity
  * improve test pipeline
* Error handling 
* Simplify the code in findig relation between films and people  

    
## Useful Links
https://docs.djangoproject.com/en/3.1/
https://docs.djangoproject.com/en/3.1/topics/testing/overview/
 
