"""usedcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from front.views import *
from usedcar import settings
from userinfo.models import UserInfo
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('url','username','email','is_staff')

class UserViewset(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

router = routers.DefaultRouter()
router.register(r'users',UserViewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userinfo.urls')),
    url(r'^sale/', include('sale.urls')),
    url(r'^buy/', include('buy.urls')),
    url(r'^index/$', index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls'),name='rest_framework')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
