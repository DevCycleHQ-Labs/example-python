"""
URL configuration for hello_togglebot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
from django.urls import path
from .views import home_page, get_variables
from .utils import log_variation

urlpatterns = [
    path("", home_page, name="home"),
    path("variables", get_variables, name="variables"),
]

is_runserver = any(arg.casefold() == "runserver" for arg in sys.argv)
if (is_runserver):
    print('Starting development server at http://127.0.0.1:8000/')
    print('Quit the server with CONTROL-C.')
    log_variation()
