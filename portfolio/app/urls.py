from django.contrib import admin
from .import views
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', views.index,name='index'),
    path('add-contact', views.contactUs,name='contact'),
    path('portfolio-detail/<int:id>/', views.portfolioDetail,name='portfolioDetail'),
    path('portfolio', PortfolioListAPIView.as_view()),
    path('aboutme/', AboutMeAPIView.as_view(), name='about_me_api'),
    path('experience/', ExperienceAPIView.as_view(), name='experience_api'),
    path('skills/', SkillsAPIView.as_view(), name='skills_api'),
    path('contact/', ContactAPIView.as_view(), name='contact_api'),
    
    # path('',include('app.urls'))
]
