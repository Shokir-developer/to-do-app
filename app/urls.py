from django.urls import path
from .views import homepage, createForm,updateForm, deleteForm

urlpatterns = [
	path('', homepage, name='home'),
	path('create/', createForm, name='create_form'),
	path('update/<str:pk>/', updateForm, name='update_form'),
	path('delete/<str:pk>/', deleteForm, name='delete_form'),
]