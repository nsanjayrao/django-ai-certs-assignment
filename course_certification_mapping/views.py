from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        mappings = CourseCertificationMapping.objects.filter(is_active=True)
        serializer = CourseCertificationMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        mapping = self.get_object(pk)
        mapping.delete()

        return Response(status=204)