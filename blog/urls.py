from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.the_blog, name = "blog"),
    path('<int:blog_id>/', views.details, name = 'detail'),

]
