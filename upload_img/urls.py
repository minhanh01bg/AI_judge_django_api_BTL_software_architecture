from django.urls import path
from .views import (
    ImageUploadView,
)

urlpatterns = [
    path('upload_img',ImageUploadView.as_view()),
]