from django.contrib import admin
from django.urls import path,include
from loginCRUD import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('update',views.update,name="update"),
    path('Edit/<int:id>',views.edit,name="edit"),
    path('Edit/update/<int:id>',views.modify,name="modify"),
    path('delet/<int:id>',views.delet,name="delete"),
    
]