from django.urls import path
from todo.views import index, todos

urlpatterns = [
	path('', todos),
	path('index/', index)
]