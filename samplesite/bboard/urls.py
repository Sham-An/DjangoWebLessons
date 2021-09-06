from django.urls import path
from .views import index, by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'), #стр 57
    path('', index, name='index'),
]