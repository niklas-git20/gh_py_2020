from django.urls import path, include
from . import views

urlpatterns = [
	path('prod_view/', views.prod_view),
	path('create_view/', views.create_view),
	path('list_view/', views.list_view),	
	# path('<id>', views.detail_view),
	path('<id>', views.update_view),
	path('<id>/delete', views.delete_view ), 
	

]