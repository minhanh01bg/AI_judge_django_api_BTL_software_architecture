from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Image
from .forms import ImageUploadForm
ALLOW_FILE_TYPES = ['jpg', 'jpeg', 'png']

class ImageUploadView(APIView):
    def post(ig, request):
        ig.upload_file(request)
        return Response(status=status.HTTP_201_CREATED)
    
    def upload_file(ig,request):
        if request.method == 'POST':
            if 'file' not in request.FILES:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            file = request.FILES['file']
            if file.size > 100000000:
                return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
            if '.' not in file.name and file.name.rsplit('.', 1)[1].lower() not in ALLOW_FILE_TYPES:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file_img = Image(Image=request.FILES['file'])
                file_img.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
            
