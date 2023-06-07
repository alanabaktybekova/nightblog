from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('category/<int:id>', category_post),
    path('post/<int:id>', post_detail),
]
