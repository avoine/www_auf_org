SESSION_COOKIE_NAME = 'sessionid_project'

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS += (
    'auf.django.references',
)

ALLOWED_HOSTS = ['localhost', 'test.www.auf.org', 'auf.org']
