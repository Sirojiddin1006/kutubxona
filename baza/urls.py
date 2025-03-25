from django.urls import path
from .views import news_list,news_detail,homePageView,contactPageView,xato,single,savol,namerequest
urlpatterns = [
    path('', homePageView, name='index'),
    path('contact/', contactPageView, name='contact'),
    path('single/<int:pk>', single, name='news_detail_page'),
    path('xato/', xato, name='xato'),
    path('news/', news_detail, name='news'),
    path('all/', news_list, name='news_list '),
    path('savol/', savol, name='savol'),
    path('namerequest/', namerequest, name='namerequest'),






]