from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import light_control
from .models import fan_control
from .models import tv_control
from .models import dh_control
from django.template import loader
from .forms import contact_form
@method_decorator(csrf_exempt, name='dispatch')
class myViews(View):
    def get(self, request):
        return HttpResponse('hello world')

@method_decorator(csrf_exempt, name='dispatch')
class Lights_config(View):
    def get(self, request):
        if request.method == 'GET':
            latest = light_control.objects.order_by('-time')[:1]
            output = ','.join([str(l.value) for l in latest])
            return JsonResponse({'value_lights' : str(output)})

    def post(self,request):
        if request.method == 'POST':
            value = request.POST.get('value_lights')
            try:
                config = light_control(value = value)
                config.save()
                return JsonResponse('saved',status=200, safe=False)
            except Exception as e:
                print(e)
                return JsonResponse('error',status=200, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class fan_config(View):
    def get(self, request):
        if request.method == 'GET':
            latest = fan_control.objects.order_by('-time_fan')[:1]
            output = ','.join([str(l.value_fan) for l in latest])
            return JsonResponse({'value_fan' : str(output)})

    def post(self, request):
        if request.method == 'POST':
            fan_value = request.POST.get('value_fan')
            try:
                config_fan = fan_control(value_fan = fan_value)
                config_fan.save()
                return JsonResponse('saved',status=200, safe=False)
            except Exception as e:
                print(e)
                return JsonResponse('error',status=200, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class tv_config(View):
    def get(self, request):
        if request.method == 'GET':
            latest = tv_control.objects.order_by('-time_tv')[:1]
            output = ','.join([str(l.value_tv) for l in latest])
            return JsonResponse({'value_tv' : str(output)})

    def post(self, request):
        if request.method == 'POST':
            tv_value = request.POST.get('value_tv')
            try:
                config_tv = tv_control(value_tv = tv_value)
                config_tv.save()
                return JsonResponse('saved',status=200, safe=False)
            except Exception as e:
                print(e)
                return JsonResponse('error',status=200, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class dh_config(View):
    def get(self, request):
        if request.method == 'GET':
            latest = dh_control.objects.order_by('-time_dh')[:1]
            output = ','.join([str(l.value_dh) for l in latest])
            return JsonResponse({'value_dh' : str(output)})

    def post(self, request):
        if request.method == 'POST':
            dh_value = request.POST.get('value_dh')
            try:
                config_dh = dh_control(value_fan = dh_value)
                config_dh.save()
                return JsonResponse('saved',status=200, safe=False)
            except Exception as e:
                print(e)
                return JsonResponse('error',status=200, safe=False)




