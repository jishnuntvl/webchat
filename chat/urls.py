
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.login,name='login'),
    path('home/<user>',views.home,name='home'),
    path('chat/<me>/<frnd>',views.chat,name='chat'),
    path('logout/',views.logout,name='logout'),
    #path('msgsnd/<me>/<frnd>',views.msgsnd,name='msgsnd'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)