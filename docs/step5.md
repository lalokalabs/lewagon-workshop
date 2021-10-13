## Step 5 - Show forms

Add this code to `views.py`:-

```
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from lewagon.models import Survey
from lewagon.forms import SurveyForm

def index(request):
    return render(request, "lewagon/index.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    form = SurveyForm(survey)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "lewagon/survey.html", context)
```

### Step 5a - Add route to urls.py

```
from lewagon.views import show_survey
```

```
path("survey/<int:id>/", show_survey, name="show-survey"),
```

### Step 5b - Add html templates

Add this code to `lewagon/templates/lewagon/survey.html`:-

```
{% extends "lewagon/base.html" %}

{% block "content" %}
<h1>{{ survey.title }}</h1>

{{ form.as_p }}

{% endblock %}
```
