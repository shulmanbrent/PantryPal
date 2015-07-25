import dj_database_url

# SendGrid Email information
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'shulmanbrent'
EMAIL_HOST_PASSWORD = 'wa2ddy123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Heroku Secret Key
SECRET_KEY = 'y1y&rrqlvwe+f1q070(gc-i21@)rubbrfjjrtdgbc)b91@*0n^'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'PantryPal DB',
#         'USER': 'postgres',
#         'PASSWORD': 'LagunaHills123',
#         'HOST': '',
#         'PORT': '5433',
#    }
# }


# Setup authentication with the Yummly servers.
YUMMLY_APP_ID = '92d67e12'
YUMMLY_API_KEY = '1c9dd40cdaa1ee28b9a65429530fcfe6'

DATABASE_URL = 'postgres://wpgqagfhkyobtb:7CitdCMz0QEFpJ70V0xbvbvqnk@ec2-50-16-229-91.compute-1.amazonaws.com:5432/d2esnf05vda63l'
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)