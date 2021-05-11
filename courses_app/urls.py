from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_course),
    path('<int:id>', views.show_course),
    path('<int:id>/destroy', views.destroy),
    path('<int:id>/confirm', views.confirm_destroy),
    path('<int:id>/comment', views.add_comment)
]