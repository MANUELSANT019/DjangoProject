from django.urls import path

urlpatterns = [
    path('', hello),
    path('about/', views.about)
]