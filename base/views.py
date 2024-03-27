from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

from random import sample

from . forms import PdfAccessForm
from . models import Personal

# Create your views here.


# @xframe_options_exempt
def home(request):
    template = loader.get_template('base/home.html')
    bg1, bg2, bg3 = sample(range(1, 4), 3)
    context = {
        'bg1': bg1,
        'bg2': bg2,
        'bg3': bg3,
        'personal_description': Personal.description,
        'interest_title': Personal.interest_title,
        'interests': Personal.interests,
        'contact_text': Personal.contact_text,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    return render(request, 'base/contact.html')


@csrf_protect
def open_pdf(request):
    if request.method == 'POST':
        form = PdfAccessForm(request.POST)
        if form.is_valid():
            pdf_path = settings.BASE_DIR / 'static' / 'redacted_CV.pdf'
            with open(pdf_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="CV_adrian_muelthaler.pdf"'
                return response
    else:
        form = PdfAccessForm()
    return render(request, 'base/open_cv.html', {'form': form})
