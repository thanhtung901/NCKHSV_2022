from django.contrib import admin

# Register your models here.
from .models import light_control
from .models import fan_control
from .models import tv_control
from .models import dh_control
admin.site.register(light_control)
admin.site.register(tv_control)
admin.site.register(dh_control)
admin.site.register(fan_control)