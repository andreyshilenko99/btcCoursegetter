import sqlite3
from rest_framework.response import Response
from getter.serializers import Serializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def get_last(request):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM response ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchone()
        conn.close()
        response_data = [{"id": result[0],
                          "course": result[1],
                          "time": str(result[2]),
                          }]
        ser_result = Serializer(response_data, many=True).data
        return Response(ser_result)


@api_view(['GET', 'POST'])
def get_all(request):
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM response"
        cursor.execute(sql)
        conn.commit()
        response_data = []
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            response_data.append({"id": row[0],
                                  "course": row[1],
                                  "time": str(row[2]),
                                  })
        print(response_data)
        conn.close()
        ser_result = Serializer(response_data, many=True).data
        return Response(ser_result)
#
