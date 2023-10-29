from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.MyCustomConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),

    ]


