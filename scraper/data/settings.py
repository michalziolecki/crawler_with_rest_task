from pathlib import Path

SEMANTIVE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cm!p&_(xiq(2!3l*hygc#kes3k&aud_q0jxaul9pl)3)4f9t9q'

# Application definition
INSTALLED_APPS = [
    'data'
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SEMANTIVE_DIR / 'restful_api/simple_rest_api' / 'db.sqlite3',
    }
}
