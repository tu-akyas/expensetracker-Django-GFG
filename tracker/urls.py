from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-transaction/<id>/', views.delete_transaction, name='delete_transaction'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup_view')
]