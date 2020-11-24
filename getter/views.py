import json
import sqlite3

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Serializer


@api_view(['GET', 'POST'])
def get_one(request):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM response ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchone()
        conn.close()
        response_data = [{"course": result[0],
                          "time": str(result[1]),
                          "id": result[2]}]
        ser_result = Serializer(response_data, many=True).data
        return Response(ser_result)


@api_view(['GET', 'POST'])
def get_all(request):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM response"
    cursor.execute(sql)
    conn.commit()
    while True:
        row = cursor.fetchone()

        if row == None:
            break
    return Response({"course": result[0],
                     "time": result[1]})
