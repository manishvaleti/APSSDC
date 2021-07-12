from django.urls import path
from RestApp import views
from django.contrib.auth import views as vs
urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('rlist/',views.restlist,name="rstl"),
    path('rstup/<int:m>/',views.rstup,name="rsup"),
    path('rstdel/<int:m>/',views.rstdel,name="rstdel"),
    path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
    path('v/',views.vx,name="vx"),
    path('ilist/',views.itlist,name="itl"),
    path('rg/',views.usrreg,name="reg"),
    path('login/',vs.LoginView.as_view(template_name="app/login.html"),name="lg"),
    path('logout/',vs.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
    path('iup/<int:m>/',views.itup,name="iup"),
    path('idel/<int:m>/',views.itdel,name="idel"),
    path('iviw/<int:a>/',views.ivw,name="ivw"),
    path('roltype/',views.rolereq,name="rlrq"),
    path('gvper/',views.gveperm, name="gvpm"),
    path('gvup/<int:t>/',views.gvupd,name="gvup"),
    path('pfle/',views.pfle,name="pf"),
    path('pfupd/',views.pfupd,name="pfud"),
    path('fdb/',views.feedback,name="fd"),
    path('reqdel/<int:t>',views.reqdel,name="rd"),
    path('chpd/',views.changepwd,name="chpd"),
]