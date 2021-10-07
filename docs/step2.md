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

### Step 2b - Test our models

```
survey1 = Survey.objects.create(title="Survey 1")
q1 = Question.objects.create(survey=survey1, text="What is capital of Japan?", pub_date=timezone.now())
q1.choice_set.add(Choice.objects.create(text="Tokyo"))

sub = Submission(survey=s1, participant_email="kamal@lalokalabs.co", participant_phonenumber="+6018712345")
```

We can list all the questions:-

```
for question in Question.objects.all():
    print(question.survey, question.text, question.pub_date)
```

and [some more data manipulation](https://docs.djangoproject.com/en/3.2/ref/models/querysets/) ...

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

## WARNING!!

`django_admin_shell` should be used for development only, never ever use it in production. And it's basically not even required for development as we can use our local console directly. For this workshop however, since we're using replit's web IDE, the console they provided has some quirky behavior sometimes.
