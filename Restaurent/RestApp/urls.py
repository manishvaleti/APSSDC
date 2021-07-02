from django.urls import path
from RestApp import views
urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('rlist/',views.restlist,name="rstl"),
    path('rstup/<int:m>/',views.rstup,name="rsup"),
    path('rstdel/<int:m>/',views.rstdel,name="rstdel"),
    path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
    path('v/',views.v,name="v"),
]