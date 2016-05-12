# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd%+j8o(ak%(&u@+o7j6b81e^o01hcm&enw@y%f3u)owe(3ol5v'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kanban',
        'USER': 'Cameron',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}
