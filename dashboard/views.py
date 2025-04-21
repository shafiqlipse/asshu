from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
# Create your views here.
def analytics(request):
    return render(request, 'dashboard/analytics.html')



@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        path = default_storage.save(f'uploads/{image.name}', ContentFile(image.read()))
        image_url = default_storage.url(path)
        return JsonResponse({'location': image_url})
