from django.urls import path

from . import views


urlpatterns = [
    path("check_pesel/", views.PESELFormView.as_view(), name="check_pesel"),
    path("pesel_result/", views.PESELResultView.as_view(), name="pesel_result"),
]
