from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from random import randint
import json
from rest_framework import status
from django.apps import apps
from django.db.models import Sum,Count,Avg,Min,Max

# Create your views here.
class postAPI(APIView):
    def post(self,request):
        try:
            dbName=request.data.get("database_name")
            data = request.data.get("data")
            
            if data.get("table_name")!=None:
                tableName=data.get("table_name")
                model = apps.get_model('post', tableName)  

                payload={}
                payload["column"]=[]
                for column in list(model._meta.get_fields()):
                    payload.get("column").append(column.name)
                
                entries = list(model.objects.using(dbName).all().values_list())
                payload["data"]=[]
                payload["length"]=0
                for e in entries:
                    payload.get("data").append(list(e))
                    payload["length"]=payload["length"]+1

                return Response(payload,status=status.HTTP_200_OK)

            else:
                if data.get("select_list")!=None:
                    payload={}
                    payload["columns"]=[]
                    for elem in data.get("select_list"):
                        payload["columns"].append(elem["column"])
                    
                    tableName=data.get("worksheet_id")
                    model = apps.get_model('post', tableName)  

                    entries = list(model.objects.using(dbName).all().values_list(*payload["columns"]))
                    payload["data"]=[]
                    payload["length"]=0
                    for e in entries:
                        payload.get("data").append(list(e))
                        payload["length"]=payload["length"]+1

                    return Response(payload,status=status.HTTP_200_OK)

                elif data.get("groupby")!=None:
                    payload={}
                    
                    payload["column"]=[]
                    for elem in data.get("groupby"):
                        payload["column"].append(elem["column"])

                    tableName=data.get("worksheet_id")
                    model = apps.get_model('post', tableName)  

                    objectMapper=model.objects.using('database1').values_list(*payload["column"])
                    args = []
                    for elem in data.get("aggregate"):
                        if elem["type"]=="sum":
                            args.append(Sum(elem["column"]))
                        elif elem["type"]=="avg":
                            args.append(Avg(elem["column"]))            
                        elif elem["type"]=="min":
                            args.append(Min(elem["column"]))
                        elif elem["type"]=="max":
                            args.append(Max(elem["column"]))
                        elif elem["type"]=="count":
                            args.append(Count(elem["column"]))   
                        elif elem["type"]=="distinct":
                            args.append(Count(elem["column"],distinct=True))

                    objectMapper = objectMapper.annotate(*args)
                    entries = list(objectMapper)
                    payload["data"]=[]
                    payload["length"]=0
                    for e in entries:
                        payload.get("data").append(list(e))
                        payload["length"]=payload["length"]+1

                    return Response(payload,status=status.HTTP_200_OK)
                
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)









