from django.contrib import admin
#from .models import UserActivities

#admin.site.register(UserActivities)
from fitternow.models import UserProfile,Activity,UserActivities,UserConsumption


admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(UserActivities)
admin.site.register(UserConsumption)



# Register your models here.
