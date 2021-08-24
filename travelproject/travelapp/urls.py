from . import views
from django.urls import path

urlpatterns = [

    #    path('',views.demo,name='demo'),
    #   path('about/',views.about,name='about'),

    # passing value throug dictionary
    #    path('india/',views.demo1,name='demo1'),

    # passing value to another page
    #    path('add/',views.add,name='add'),

    #    path('addition/',views.addition,name='addition'),

    # djangostatic website
    path('', views.web, name='web')

]
