from rest_framework.views import APIView
from django.http import JsonResponse
from services.utils import csv_reader


class MLView(APIView):
    def post(self, request):
        csv_file = request.FILES['file_path']
        result = csv_reader(csv_file)
        return JsonResponse({'result': result})
