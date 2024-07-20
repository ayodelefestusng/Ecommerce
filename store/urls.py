from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
     path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_views.LoginView.as_view(template_name='logout.html'), name='logout'),


	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]