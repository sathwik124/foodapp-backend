from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.getfooddata),
    path('getc/<id>/',views.getidfooddata),
    path('get/<id>/',views.getcartdata),
    path('add/',views.addcartdata),
    path('delete/<id>/',views.remcartdata),
    path('login/',views.userlogin),
    path('signup/',views.usersignup),
    path('allreviews/<id>/',views.getallrevs),
    path('putreview/',views.putrev),
    path('rate/<id>/',views.getrate)
    # path('username/',views.getusername),
    # path('logout/',views.logout_view),
    # path('islog/',views.islogged),
]