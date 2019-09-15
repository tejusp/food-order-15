"""Eatrip URL Configuration

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
from django.conf import settings  # these two are for uploading media.
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views  # setting alias with use of views.

from EatripApp import views, apis

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
                  url(r'^restaurant/sign-in/$', auth_views.LoginView,
                      # using auth_views django will take are of authentication algorithms
                      {'template_name' : 'restaurant/sign_in.html'},
                      name = 'restaurant-sign-in'),
                  url(r'^restaurant/sign-out', auth_views.LogoutView,
        {'next_page' : '/'},
        name = 'restaurant-sign-out'),
    url(r'^restaurant/$', views.restaurant_home, name=  'restaurant-home'),
    url(r'^restaurant/sign-up',views.restaurant_sign_up,
        name = 'restaurant-sign-up'),

    url(r'^restaurant/account/$', views.restaurant_account, name = 'restaurant-account'),
    url(r'^restaurant/meal/$', views.restaurant_meal, name = 'restaurant-meal'),
    url(r'^restaurant/order/$', views.restaurant_order, name = 'restaurant-order'),
    url(r'^restaurant/report/$', views.restaurant_report, name = 'restaurant-report'),
    url(r'^restaurant/meal/add/$', views.restaurant_add_meal, name = 'restaurant-add-meal'),
    url(r'^restaurant/meal/edit/(?P<meal_id>\d+)$', views.restaurant_edit_meal, name = 'restaurant-edit-meal'),
    #For sign-up/sign-out/sign-out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/restaurant/order/notification/(?P<last_request_time>.+)/$', apis.restaurant_order_notification),

    #/convert token (sign-in/sign-up)
    #/revoke-token (sign-out)

    #Apis for customer
    url(r'^api/customer/restaurant/$', apis.customer_get_restaurants),
    url(r'^api/customer/meals/(?P<restaurant_id>\d+)/$', apis.customer_get_meals),
    url(r'^api/customer/order/$', apis.customer_add_order),
    url(r'^api/customer/order/lastest/$', apis.customer_get_lastest_order),
    url(r'^api/customer/driver/location/$', apis.customer_driver_location ),

    #API for Driver
    url(r'^api/driver/orders/ready/$', apis.driver_get_ready_orders),
    url(r'^api/driver/order/pick/$', apis.driver_pick_orders),
    url(r'^api/driver/order/latest/$', apis.driver_get_latest_orders),
    url(r'^api/driver/order/complete/$', apis.driver_complete_orders),
    url(r'^api/driver/revenue/$', apis.driver_get_revenue),
    url(r'^api/driver/location/update/$', apis.driver_update_location),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
