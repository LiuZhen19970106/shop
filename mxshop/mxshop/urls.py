"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
import xadmin
from mxshop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodViewSet, GoodsCategoryViewset, BannerViewset, IndexCategoryViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset

router = DefaultRouter()

# 配置goods的url
router.register('goods', GoodViewSet, basename='goods')

# 配置category的url
router.register('category', GoodsCategoryViewset, basename='category')

# 收藏
router.register('userfavs', UserFavViewset, basename='userfavs')

# 留言
router.register('messages', LeavingMessageViewset, basename='messages')

# 收货地址
router.register('address', AddressViewset, basename='address')

# 购物车地址
router.register('shopcart', ShoppingCartViewset, basename='shopcart')

# 订单地址
router.register('orders', OrderViewset, basename='orders')

# 轮播图地址
router.register('banners', BannerViewset, basename='banners')

# 首页商品系列数据地址
router.register('indexgoods', IndexCategoryViewset, basename='indexgoods')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls')),

    path('', include(router.urls)),

    path('login', obtain_jwt_token),

    path('docs/', include_docs_urls(title='b'))
]
