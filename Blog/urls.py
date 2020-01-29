
from django.urls import path
from .views import Blog, detail

app_name = "Blog"
urlpatterns = [
    path('',Blog, name = 'Blog'),
    path('<int:blog_id>/',detail,name = 'detail'),
   

]
