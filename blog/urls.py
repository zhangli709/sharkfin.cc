from django.conf.urls import url

from blog import views

urlpatterns = [
    # 主页，闪购，购物车，个人中心
    url(r'', views.home, name='home'),
]