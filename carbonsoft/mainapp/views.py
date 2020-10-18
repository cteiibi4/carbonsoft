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


def main(request):
    title = 'Главная'

    parametrs = SystemParametrs.objects.all()
    all_parametrs = []
    for i in parametrs:
        all_parametrs.append(i.cpu)
    last_parametrs = all_parametrs[-1:-101:-1]
    min_cpu = min(all_parametrs)
    max_cpu = max(all_parametrs)
    avg_cpu = sum(all_parametrs)/len(all_parametrs)
    min_cpu_last = min(last_parametrs)
    max_cpu_last = max(last_parametrs)
    avg_cpu_last = sum(last_parametrs)/len(last_parametrs)

    content = {'title': title, 'all_parametrs': all_parametrs,
               'last_parametrs': last_parametrs, 'min_cpu': min_cpu,
               'max_cpu': max_cpu, 'avg_cpu': avg_cpu,
               'min_cpu_last': min_cpu_last, 'max_cpu_last': max_cpu_last,
               'avg_cpu_last': avg_cpu_last}
    return render(request, 'mainapp/index.html', content)
