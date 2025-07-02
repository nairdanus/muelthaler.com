from django.contrib import admin
from django.urls import path, include

from .views import scroll_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scroll_page_view, name='scroll-page'),
]
