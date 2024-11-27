import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from .models import BaseStation
from .serializers import BaseStationSerializer


class UploadFileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "Файл не найден."}, status=400)

        try:
            df = pd.read_excel(file)
            df['technology'] = df['technology'].fillna('')  # Можно заменить на любой дефолт

            for _, row in df.iterrows():
                BaseStation.objects.create(
                    ne=row['ne'],
                    address=row['address'],
                    coordinates=row['coordinates'],
                    technology=row['technology'],  # Строка, например 'lte, gsm'
                    status=row['status'],
                )

            return Response({"message": "Данные успешно загружены!"})
        except Exception as e:
            return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def get_data_json(request):
    stations = BaseStation.objects.all()
    serializer = BaseStationSerializer(stations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_html(request):
    stations = BaseStation.objects.all()
    return render(request, 'api/table.html', {'stations': stations})

