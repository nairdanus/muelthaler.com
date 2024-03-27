from django.urls import path


from . views import home, contact, open_pdf

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('cv/', open_pdf, name='open_pdf'),
]
