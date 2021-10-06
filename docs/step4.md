## Step 4 - Define forms

```
from django import forms
from mysite.models import Submission, Choice

class SurveyForm(forms.Form):
    email = forms.EmailField()
    phonenumber = forms.CharField()
    question_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=())

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        for question in survey.question_set.all():
          choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
          self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
          self.fields[f"question_{question.id}"].label = question.text
```

### Step 4a - Test forms in web console

```
from mysite.forms import SurveyForm
from mysite.models import Survey

survey = Survey.objects.all()[0]
data = {
    "email": "kamal@lalokalabs.co",
    "phonenumber": "+81919191919",
    "question_1": "1",
    "question_2": "4",
}
form = SurveyForm(survey, data)
if form.is_valid():
    print(form.cleaned_data)
else:
    print(form.errors)

print(form.fields["question_2"].choices)
```