from django.urls import path
from .views import UploadFileView, get_data_json, get_data_html

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('data/json/', get_data_json, name='data-json'),
    path('data/html/', get_data_html, name='data-html'),
]
