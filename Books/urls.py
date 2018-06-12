from django.conf.urls import url
from .import views
urlpatterns = [
url(r'^$',views.hello),
url(r'^Login',views.Login),
url(r'^Register',views.Register),
url(r'^Home',views.Home),
url(r'^About',views.About),
url(r'^Contact',views.Contact),
url(r'^Search-form/$',views.search_form),
url(r'^search/$', views.search),
]