# Bookstore

### Installation

1. Install Django
   ```sh
   pip install django
   ```
2. Install Mysqlclient
   ```sh
   pip install mysqlclient
   ```
3. Install Django Widget Tweaks
   ```sh
   pip install django-widget-tweaks
   ```
4. Set your MySQL configuration in `Bookstore/settings.py`
   ```py
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.mysql', 
         'NAME': YOUR_DB_NAME,
         'USER': YOUR_DB_USER,
         'PASSWORD': YOUR_DB_PASSWORD,
         'HOST': 'localhost',   
         'PORT': '3306',
      }    
   }
   ```
5. Run migrations
   ```sh
   python manage.py migrate
   ```
6. Running the Local Development Server
   ```sh
   python manage.py runserver
   ```
