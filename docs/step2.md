## Step 2 - Setup admin site

Create super user:-

```
poetry run python manage.py createsuperuser
```


### Step 2a - Uncomment url to admin shell

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
