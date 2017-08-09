from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from regform.models import Profile
from regform.forms import UserProfileForm

def homepage(request):
    return render(request , 'regform/homepage.html')


def register(request):
    registered = False

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        profile = profile_form.save(commit=False)
        profile.save()

        registered = True

    else:
        profile_form = UserProfileForm()
    return render(request,
                  'regform/register.html',
                  {'profile_form': profile_form, 'registered': registered})
