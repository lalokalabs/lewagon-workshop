## Step 5 - Show forms

Add this code to `views.py`:-

```
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from mysite.models import Survey
from mysite.forms import SurveyForm

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "mysite/survey.html", context)
```

Add this code to `mysites/templates/mysite/survey.html`:-

```
{% extends "mysite/base.html" %}

{% block "content" %}
<h1>{{ survey.title }}</h1>

{{ form.as_p }}

{% endblock %}
```
