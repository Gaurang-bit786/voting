from .views  import *
from django.urls import path

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', index, name='index'),
    path('save_vote/', save_vote, name='save_vote'),
    path('analysis/', analysis, name='analysis'),
    path('voters/', voters, name='voters'),
    path('details/<int:id>/', show_details, name='show_details'),
    path('analysis/<str:cat>/', analysis_data, name='analysis_data'),
]
