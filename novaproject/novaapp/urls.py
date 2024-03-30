from django.urls import path
from .views import index, about, blogdetails, blog, contact, portfolioDetails, portfolio, services, team

urlpatterns = [
  path('',index, name='home'),
  path('about-us/',about, name='about'),
  path('blog-details/',blogdetails, name='blog-details'),
  path('blog-us/',blog, name='blog'),
  path('contact-us/',contact, name='contact'),
  path('portfolio-details/',portfolioDetails, name='portfolio-details'),
  path('portfolio-us/',portfolio, name='portfolio'),
  path('services-us/',services, name='services'),
  path('team-us/',team, name='team'),

]