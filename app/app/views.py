from django.shortcuts import render
from rest_framework import views
from app.serializers import DiseaseParametersSerializer
from django.views import View
from app.forms import patient_record
import pandas as pd
import pickle

def index(request):
    return render(request, "index.html")

class PatientRecordViewset(views.APIView):

    def get(self, request, *args, **kwargs):
        form = patient_record.Record()
        return render(request, 'form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        serializer = DiseaseParametersSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            data = {
                'Feature_2':[record.feature_2],
                'Feature_3':[record.feature_3],
                'Feature_4':[record.feature_4],
                'Feature_5':[record.feature_5],
                'Feature_37':[record.feature_37],
                'Feature_43':[record.feature_43],
                'Feature_44':[record.feature_44]
            }
            model = pickle.load(open("/app/app/SDSP_RandomForestClassifierModel.sav", 'rb'))
            pred = model.predict_proba(pd.DataFrame(data, columns=['Feature_2','Feature_3','Feature_4','Feature_5','Feature_37','Feature_43','Feature_44']))
            return render(request, 'result.html', dict(zip(['Disease_1', 'Disease_2', 'Disease_3', 'Disease_4'], pred[0])))

    

