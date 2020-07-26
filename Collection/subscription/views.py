from django.shortcuts import render,HttpResponseRedirect,reverse
from .validation_utility import validate_email
# Create your views here.


def subscribe(request):

    post_data = request.POST.copy()
    email = post_data.get("email", None)
    error_msg = validation_utility.validate_email(email)
    if error_msg:
        messages.error(request, error_msg)
        return HttpResponseRedirect(reverse('appname:subscribe'))