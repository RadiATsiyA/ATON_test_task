from django.urls import path
from Users import views


app_name = 'Users'


urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login'),
    path('clients/', views.ClientsListView.as_view(), name='clients'),
    path('update_status/<int:pk>', views.UpdateStatusView.as_view(), name='update_status')
]