## Step 3 - Add models to admin site

```
from django.contrib import admin
from mysite.models import Survey, Question, Choice, Submission

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True

class ChoiceInline(admin.TabularInline):
  model = Choice


class SurveyAdmin(admin.ModelAdmin):
  inlines = [
    QuestionInline
  ]

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
```
