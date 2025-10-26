from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . views import home, contact, open_pdf, parallax

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('cv/', open_pdf, name='open_pdf'),
    path('parallax/', parallax, name='parallax'),
    path('goals/', include('goal.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
