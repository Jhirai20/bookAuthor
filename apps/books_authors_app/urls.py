from django.conf.urls import url
from. import views
#always remember to add comma
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addBook$', views.addBook),
    url(r'^books/(?P<id>\w+)$', views.books)
]