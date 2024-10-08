from django.urls import path

from . import views


urlpatterns = [
    path("upload_file/", views.UploadFileFormView.as_view(), name="upload_file"),
]
