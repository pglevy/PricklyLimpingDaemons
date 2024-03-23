from django.urls import path
from things import views

urlpatterns = [path("", views.thing_index, name="thing_index")]
