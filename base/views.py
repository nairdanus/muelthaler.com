from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from random import sample

# Create your views here.


# @xframe_options_exempt
def home(request):
    template = loader.get_template('base/home.html')
    bg1, bg2, bg3 = sample(range(1, 4), 3)
    context = {
        'bg1': bg1,
        'bg2': bg2,
        'bg3': bg3,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    return render(request, 'base/contact.html')
