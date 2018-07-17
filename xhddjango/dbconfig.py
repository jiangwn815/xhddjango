def db():
    config = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_test5',
            'USER': 'root',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    return config
