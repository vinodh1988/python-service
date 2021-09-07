
from django.urls import path
from firstrest.views import hello
urlpatterns = [
    path('hello/',hello,name="hello-item")
]