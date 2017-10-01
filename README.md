# CristianBlog


CristianBlog is my personal blog created with the intention to help the open source community by providing useful information regarding different packages for python.


## Getting Started

To de get the source code up running, clone the git repo.

  
      git clone https://github.com/cristiangabor/Blog-.git

### Prerequisites

  These are the following packages required for blog in order to run. 
  
  1. virtualenv.
  2. django-pagedown.
  3. django-markdown-deux.
  4. mysqlclient (for using mysql as database).
  
  
  
### Installing

  Installing them using pip package manager...
  
  `pip install virtualenv`
  
  Setting up virtualenv...
  
  ```
  cd Blog-
  virtualenv -p /usr/bin/python3.6 Blog
  source Blog/bin/activate
  ```
  
  *To exit the virtual enviroment type:
  `deactivate`
  
  ```
  pip install django-pagedown
  pip install django-markdown-deux
  pip install mysqlclient
  ```
  To set ``django-pagedown`` edit ``settings.py``.
  
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party library
    'pagedown',
]
```

  To set ``django-markdown-deux`` edit ``INSTALLED_APS`` again. 
  
   ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    #third party library
    'pagedown',
    'markdown_deux',
]
```

  Using MySQL
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_username>$<your_database_name>',
        'USER': '<your_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': '<your_mysql_hostname>',
    }
}
```
  
  
  
  
  


  
