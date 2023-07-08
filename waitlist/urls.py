
from django.contrib import admin
from django.urls import path
from waitlist_form.views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('waitlist/', Waitlist, name = "waitlist"),
    path('', TemplateView.as_view(template_name='index.html')),


]
