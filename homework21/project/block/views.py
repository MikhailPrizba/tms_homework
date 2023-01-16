import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests


class MyClassBasedView(View):
    list1 = []
    count = 0
    def get(self, request, *args, **kwargs):
        if kwargs:
            number = kwargs['num']
        else:
            number = 1
        
        self.list1 = [requests.get('https://api.kanye.rest').json()['quote'] for self.count  in range(int(number))]
        answer = ' \n'.join(self.list1)
        return HttpResponse(answer)

def factorial(n):
    if(n<=1):
        return 1
    else:
        return(n * factorial(n-1))


@csrf_exempt
@require_http_methods(['GET','POST'])
def index(request):
    data = json.loads(request.body)
    num = data['number']
    answer = factorial(int(num))
    data['factorial'] = answer
    back = json.dumps(data)
    return HttpResponse(back)
   