from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/',views.index,name="index"),
    url(r'^post/',views.post_page,name="post_page"),
    url(r'^dopost/',views.do_post_page,name="do_post_page"),
    url(r'^getcontent/',views.get_content,name="get_content"),
    url(r'^home/',views.home,name="home"),
    url(r'^login/',views.login,name="login"),
    url(r'^logout/',views.logout,name="logout"),
]