from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SystemParametrs
from.serializers import SystemParametrsSerializer


# Create your views here.
class SystemView(APIView):
    def post(self, request):
        cpu = request.data
        print(cpu)

        serializer = SystemParametrsSerializer(data=cpu)
        if serializer.is_valid(raise_exception=True):
            cpu_saved = serializer.save()
        return Response({'success': f'CPU {cpu_saved.cpu} added'})
