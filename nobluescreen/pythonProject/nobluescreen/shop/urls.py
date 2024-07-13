# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('feedback/new/', views.CreateFeedbackView.as_view(), name='feedback_create'),
    path('feedback/<int:pk>/edit/', views.UpdateFeedbackView.as_view(), name='feedback_update'),
    path('feedback/<int:pk>/delete/', views.DeleteFeedbackView.as_view(), name='feedback_delete'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('checkout/process/', views.process_checkout, name='process_checkout'),
    path('contact/', views.contact_view, name='contact'),
    path('platform/<str:category>/', views.GamePlatformView.as_view(), name='game_platform'),
]
