from django.urls import path

from .views import LogView
from .views import SingleLogView


app_name = "logs"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('logs/', LogView.as_view()),
    path('logs/<int:pk>', LogView.as_view()),
    path('logs/<int:pk>', SingleLogView.as_view()),
]