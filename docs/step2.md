## Step 2 - Setup admin site

Create super user:-

```
poetry run python manage.py createsuperuser
```


### Step 2a - Uncomment url to admin shell in urls.py

```
urlpatterns = [
    #path("", lewagon.views.index),
    path('admin/', admin.site.urls),   
]

if settings.DEBUG:
    urlpatterns = [
        re_path(r'^admin/shell/', include('django_admin_shell.urls')),
    ] + urlpatterns
```

## Notes

Ensure `django_admin_shell` added to `INSTALLED_APPS` settings:-

```
INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lewagon',
    'django_admin_shell',
]
```
