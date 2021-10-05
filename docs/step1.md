## Step 1 - Define models

```
from django.db import models

class Survey(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.text
poetry run python manage.py makemigrations lewagon
  def __str__(self):
    return self.text

class Choice(models.Model):
  question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.question.text}:{self.text}"

class Submission(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  participant_email = models.EmailField(max_length=255)
  participant_phonenumber = models.CharField(max_length=255)
  answer = models.ManyToManyField(Choice)

```

### Step 1a - Create migrations

```
poetry run python manage.py makemigrations lewagon
```
