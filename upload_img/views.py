from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Image
from .forms import ImageUploadForm
from models import evaluate
import numpy as np
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
ALLOW_FILE_TYPES = ['jpg', 'jpeg', 'png']

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(operation_description='Upload attack file...',
                         manual_parameters=[openapi.Parameter(
                             name="file",
                             in_=openapi.IN_FORM,
                             type=openapi.TYPE_FILE,
                             required=True,
                             description="files"
                         )])
    def post(ig, request):
        # ig.upload_file(request)
        return ig.upload_file(request)
    
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

            labels = ['bag', 'dress', 'flats', 'hat', 'heels', 'jacket', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 'sneakers', 'tshirt']
            # result = 0
            if form.is_valid():
                file_img = Image(Image=request.FILES['file'])
                file_img.save()
                result = evaluate.run_example(file.name)
                result = np.argmax(result, axis=-1)
                print(result)
                # return Response(status=status.HTTP_201_CREATED)
                print(labels[result[0]])
                
                return Response(labels[result[0]])
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
            