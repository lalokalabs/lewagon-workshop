## Step 6 - Process data submitted via forms

The whole views code should be like this:-

```
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from lewagon.models import Survey
from lewagon.forms import SurveyForm

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)

    url = reverse("show-survey", args=(id,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "lewagon/survey.html", context)
```

And the templates should looks like this:-

```
{% extends "lewagon/base.html" %}

{% block "content" %}
<h1>{{ survey.title }}</h1>

<form action="{% url 'show-survey' survey.id %}" method="POST">
{% csrf_token %}
{{ form.as_p }}
<input type="submit" name="submit" value="Submit" />
</form>
{% endblock %}
```

### Step 6a - Add logic to save the data in forms

```
from django import forms
from lewagon.models import Submission, Choice

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

    def save(self):
      data = self.cleaned_data
      submission = Submission(survey=self.survey, participant_email=data["email"], participant_phonenumber=data["phonenumber"])
      submission.save()
      for question in self.survey.question_set.all():
          choice = Choice.objects.get(pk=data[f"question_{question.id}"])
          submission.answer.add(choice)
      
      submission.save()
      return submission
```
