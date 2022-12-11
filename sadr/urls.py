
from django.contrib import admin
from django.urls import path
from sadrapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('gg/', views.gettutorial),
    # path('postuser/', views.postuser),
    path('', views.index),
    path('appointment', views.index),
    path('form', views.form),
    path('order', views.order)
]

