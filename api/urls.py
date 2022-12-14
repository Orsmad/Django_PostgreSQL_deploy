from django.urls import path
from . import views

urlpatterns = [
    # all urls
	path('', views.apiOverview),

    # crud
	path('notes/', views.notes),
	path('notes/<pk>', views.notes)
]