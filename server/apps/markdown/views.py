from django.shortcuts import redirect, render
import markdown
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def result_ajax(request):
    if request.method == 'POST':
        print('here')
        print(request.body)
        req = json.loads(request.body)
        id = req['id']
        textMD = req['textMD']
        html = markdown.markdown(textMD, extensions=['fenced_code', 'codehilite'])
        print(html)
        return JsonResponse({'id': id, 'content': html})
    
    return redirect('/')