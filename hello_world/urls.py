from django.urls import path
from hello_world import views
#grdhthtr
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
