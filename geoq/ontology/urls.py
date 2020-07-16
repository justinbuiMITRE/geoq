from django.urls import include, re_path, path
from django.contrib.auth.decorators import login_required
#from .views import ProxyListView, ProxyRegisterView, ProxyGetView, ProxyAuxGetView
from .views import *

urlpatterns = [
    #re_path(r'(?P<url>.*)/$', ProxyListView.as_view(), name='list'),
    path('semanticQueryInfo/', semanticQueryInfo(), name ='semanticQueryInfo'),
    #path('register', login_required(ProxyRegisterView.as_view()),name="register"),
    #path('kmz/(.+)/', ProxyGetView.as_view(),name="getkmz"),
    #path('kmz/(.+)/',ProxyGetView,name="getkmz"),
    #path('image/(\w+)/(\w+)/', ProxyAuxGetView.as_view(),name="auxget")
]
