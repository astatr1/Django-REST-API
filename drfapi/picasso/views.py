from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .tasks import upload_file

from .models import File
from .serializers import FileSerializer


class FileAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileUploadView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    file_serializer = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.file_serializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            upload_file.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
