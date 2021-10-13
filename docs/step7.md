## Step 7 - Verify email using GETOTP

```
import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

import requests

from lewagon.models import Survey, Submission
from lewagon.forms import SurveyForm

def index(request):
    return render(request, "lewagon/index.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)

    url = reverse("show-survey", args=(id,))
    otp_redirect_url = request.build_absolute_uri(url)
    otp_callback_url = request.build_absolute_uri(reverse("otp-callback"))
    if form.is_bound and form.is_valid():
        data = form.cleaned_data
        submission = form.save()
        url = send_otp(submission, data["email"], otp_redirect_url, otp_redirect_url, otp_callback_url)
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "lewagon/survey.html", context)


def send_otp(submission, email, success_url, fail_url, callback_url):
    params = {
        "channel": "email",
        "email": email,
        "callback_url": callback_url,
        "success_redirect_url": success_url,
        "fail_redirect_url": fail_url,
        "metadata": submission.id,
    }


    auth = (settings.GETOTP_API_SID, settings.GETOTP_API_TOKEN)
    resp = requests.post("https://otp.dev/api/verify/", data=params, auth=auth)
    data = resp.json()
    redirect_url = data["link"]
    return redirect_url
    
@csrf_exempt
def otp_callback(request):
    data = json.loads(request.body)
    submission_id = int(data["metadata"])
    email = data["email"]
    auth_status = data["auth_status"]

    submission = get_object_or_404(Submission, pk=submission_id, participant_email=email)
    submission.status = auth_status
    submission.save()
    return HttpResponse("OK")
```

### Step 7a - Add url route to urls.py

```
path("survey/otp/callback/xtygyita/", otp_callback, name="otp-callback"),
```
    
### Step 7b - Add GETOTP API Key and Auth token to settings.py
    
 ```
GETOTP_API_SID = os.environ.get('GETOTP_API_SID', None)
GETOTP_API_TOKEN = os.environ.get('GETOTP_API_TOKEN', None)
```
