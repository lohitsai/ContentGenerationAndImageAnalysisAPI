from django.urls import path
from Product_Desc.views import ProductDesc, ImageAnalyze

urlpatterns = [
    path("product/<str:title>/", ProductDesc),
    path("image/", ImageAnalyze.as_view()),
]
