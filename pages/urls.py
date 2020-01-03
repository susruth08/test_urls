from django.urls import path
from . import views
app_name = 'math'
urlpatterns = [
path('', views.home, name='home'),
path('long_addition/',views.long_addition,name='long_addition'),
path('long_addition/long_additions/',views.long_additions,name='long_additions'),
path('lcm_more/',views.lcm_more,name='lcm_more'),
path('lcm_more/lcm_more1/',views.lcm_more1,name='lcm_more1'),
]