from django.urls import path, include
from . import views
urlpatterns = [
        path('',views.index),
        path('him/',views.him,name='him'),


]