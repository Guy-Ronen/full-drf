from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list_create_api_view),
    path("<int:pk>/", views.product_detail_api_view),
    path("<int:pk>/update/ ", views.product_update_api_view),
    path("<int:pk>/delete/", views.product_delete_api_view),
]
