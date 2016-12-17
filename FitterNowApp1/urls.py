"""FitterNowApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from fitternow.appviews import UserViewSet,RegisterUserViewSet,LoginUserViewSet,ActivityViewSet,food_search, \
    UserProfileUpdateViewSet, UserProfileDetailViewSet, UserConsumptionViewSet, UserConsumptionDetailViewSet, \
    UserActivitesViewSet, UserActivitiesListViewSet
from fitternow.appviews import UserProfileViewSet
# ,UserProfileDetailViewSet, UserActivitesViewSet,UserActivitiesListViewSet,UserProfileUpdateViewSet,UserConsumptionViewSet,UserConsumptionDetailViewSet
from fitternow import appviews
#
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
#
router.register(r'UserProfile', UserProfileViewSet)
router.register(r'UserProfileUpdate',UserProfileUpdateViewSet)
router.register(r'UserProfileDetail', UserProfileDetailViewSet)

router.register(r'UserConsumption', UserConsumptionViewSet)
router.register(r'UserConsumptionDetail', UserConsumptionDetailViewSet)
#
router.register(r'Activity', ActivityViewSet)
#
router.register(r'UserActivities', UserActivitesViewSet)
router.register(r'UserActivitiesList', UserActivitiesListViewSet)


#router.register(r'UserActivities/(?P<id>\d+)/?$',UserActivitiesViewSet, base_name="UserActivities")
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^register/$',views.CreateUserView.as_view(), name='user'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', RegisterUserViewSet.as_view(), name='register'),
    url(r'^login/$', LoginUserViewSet.as_view(), name='login'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'search/$', appviews.food_search),
    url(r'getmeasures/$', appviews.get_measure),
    url(r'getnutrients/$', appviews.get_nutrients)
]

