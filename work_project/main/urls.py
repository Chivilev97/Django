from django.urls import include, path, re_path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin', admin.site.urls),
    path('foo/bar/apple', views.page, name='apples'),
    path('foo/bar/dfdfd', views.page, name='mandarina'),
    re_path(r'', views.page, name='menu'),
]