from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserProfile,Activity,UserActivities,UserConsumption
from rest_framework.authtoken import views


User =get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')

class RegisterUserSerializer(serializers.ModelSerializer):
        username = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.CharField()

        class Meta:
            model = User
            fields = ['username','first_name', 'last_name', 'email', 'password']
            extra_kwargs = {"password" : {"write_only": True}}

        def create(self, registration_data):
            username = registration_data['username']
            first_name = registration_data['first_name']
            last_name = registration_data['last_name']
            email = registration_data['email']
            password = registration_data['password']
            user_obj = User(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            user_obj.set_password(password)
            user_obj.save()
            return registration_data


        def validate(self, data):
            email = data['email']
            user_qs = User.objects.filter(email=email)
            if user_qs.exists():
                raise serializers.ValidationError("This account is taken")
            return data

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {"password" : {"write_only": True}}

    def validate(self,data):
        user_data = None
        username = data.get("username",None)
        password = data['password']
        user = (User.objects.filter(username = username)).exclude(username__isnull = True).exclude(username__iexact='')
        if user.count()==1 and user.exists():
            user_data = user.first()
        else:
            raise serializers.ValidationError("Invalid username")

        if user_data:
            if not user_data.check_password(password):
                raise serializers.ValidationError("Incorrect password")

        return data

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = UserProfile
        fields= ('user','date_created','date_of_birth','gender','height','weight','user_notes','secure_quest','secure_answer')

class UserConsumptionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model= UserConsumption
        fields= ('user','date_created','nbdno','food_name','food_calories')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_name', 'calories')

class UserActivitiesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = UserActivities
        fields = ('user','activity_name','duration','calories_burned')
















                #password = serializers.CharField(write_only=True)
#override
    #def create(self,validated_data):
     #   user = get_user_model().objects.create(
      #      username = validated_data['username']
       # )
        #user.set_password(validated_data['password']) #hash
        #user.save()
        #return user

   # class Meta:
    #    model = get_user_model()
     #   fields= ('username','password')

