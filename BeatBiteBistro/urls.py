"""BeatBiteBistro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from BeatBiteBistroapi.views import CustomerView
from BeatBiteBistroapi.views import ItemView
from BeatBiteBistroapi.views import OrderItemView
from BeatBiteBistroapi.views import check_user, register_user, delete_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"customers", CustomerView, "customer")
router.register(r"items", ItemView, "item")
router.register(r"order_items", OrderItemView, "order_item")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("checkuser", check_user),
    path("registeruser", register_user),
    path("deleteuser/<int:user_id>/", delete_user),
]
