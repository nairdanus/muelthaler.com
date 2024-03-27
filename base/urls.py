from django.urls import path


from . views import home, contact, open_pdf

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('open_pdf/', open_pdf, name='open_pdf'),
]
