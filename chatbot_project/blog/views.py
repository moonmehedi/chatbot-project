from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here



def index(req):
    return render(req,'index.html')


def specific(request):
    return HttpResponse('this is the specific urls ')


    
    
    

@csrf_exempt  # Temporarily exempt from CSRF for testing purposes (not recommended for production)
def getResponse(request):
        
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            message=data.get('message','')
            print('Received message:',message)
            
            return JsonResponse({'message':message})
        except json.JSONDecodeError:
            return JsonResponse({'error':'Invalid JSON'},status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)





