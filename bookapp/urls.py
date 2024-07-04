from django.urls import path
from.import views
urlpatterns = [
    path("",views.index, name="index"),
    path("delete/<id>",views.delete_,name="dalete_"),
    path('edit/<int:pk>/',views.edit_,name="edit_")
]
