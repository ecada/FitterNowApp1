from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import UserProfile,Activity,UserActivities,UserConsumption
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics
from .apiwrapper import FCD
from .Serializers import UserSerializer, RegisterUserSerializer, LoginUserSerializer,ActivitySerializer,UserActivitiesSerializer,UserConsumptionSerializer
from .Serializers import UserProfileSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken import views

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUserViewSet(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

class LoginUserViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) # to perform CRUD operations.
    queryset = UserProfile.objects.all()#.order_by('-date_created')
    model = UserProfile
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset


    def perform_create(self, serializer):
        """
        Make the current user PROFILE DETAIL owner
        :param serializer:
        :return:
        """
        return serializer.save(user=self.request.user)

class UserProfileUpdateViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) # to perform CRUD operations.
    queryset = UserProfile.objects.all().order_by('-date_created')
    model = UserProfile
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset


    def perform_update(self, serializer):
        """
        Make the current user PROFILE DETAIL owner
        :param serializer:
        :return:
        """
        return serializer.save(user=self.request.user)

class UserProfileDetailViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    model = UserProfile
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset

class ActivityViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Activity.objects.all()
    model = Activity
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

class UserActivitesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) # to perform CRUD operations.
    queryset = UserActivities.objects.all().order_by('-date_created')
    model = UserActivities
    serializer_class = UserActivitiesSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset


    def perform_create(self, serializer):
        """
        Make the current user PROFILE DETAIL owner
        :param serializer:
        :return:
        """
        return serializer.save(user=self.request.user)

class UserActivitiesListViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserActivities.objects.all().order_by('-date_created')
    model = UserActivities
    serializer_class = UserActivitiesSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user).order_by('-date_created')
        return queryset

#Below function is from Mustafa Atik's course on Django
@csrf_protect
def food_search(request):
    keyword = request.GET["q"]
    items = FCD.find(keyword)
    return HttpResponse(json.dumps(items), content_type="application/json")

@csrf_protect
def get_measure(request):
    keyword = request.GET["m"]
    measures = FCD.get_measures(keyword)
    return HttpResponse(measures, content_type="application/json")

@csrf_protect
def get_nutrients(request):
    keyword = request.GET["n"]
    nutrition = FCD.get_nutrients(keyword)
    return HttpResponse(nutrition, content_type="application/json")

class UserConsumptionViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) # to perform CRUD operations.
    queryset = UserConsumption.objects.all().order_by('-date_created')
    model = UserConsumption
    serializer_class = UserConsumptionSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset


    def perform_create(self, serializer):
        """
        Make the current user PROFILE DETAIL owner
        :param serializer:
        :return:
        """
        return serializer.save(user=self.request.user)

class UserConsumptionDetailViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserConsumption.objects.all()
    model = UserConsumption
    serializer_class = UserConsumptionSerializer
    def get_queryset(self):
        """
        returns the PROFILE DETAILS of the current user
        """
        queryset = self.model.objects.all().filter(user=self.request.user)
        return queryset