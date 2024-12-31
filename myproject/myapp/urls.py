# from django.urls import  path
# # from current directory import the views.py in oder to map to the index function
# # from that index function returns the http response with text which will be rendered on the page
# from . import views

# # define a list for the url patterns
# # listof urls that the user wants to navigate to, all routes that are going to be available in our applications
# urlpatterns = [
#     # go to views.py access the index function and trigger/invoke it to return the http response to render what it has to the browser
#     path('', views.index)
# ]

# from django.urls import  path
# from .views import index

# urlpatterns = [
#     path('', index, name="index"),
# ]

from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success'),
]

