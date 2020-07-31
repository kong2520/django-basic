"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('photo.urls')),
    path('accounts/',include('accounts.urls'))
]

# 이건 서버 작업할땐 불필요한 작업이다. 디버깅 모드가 끄게 되면 이게 정상적으로 작동하지않는다.
# 실제로는 이미지서버를 이용한다.
# MEDIA_URL로 들어오는 url은 document_root에서 찾아주세요 라는 뜻
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)