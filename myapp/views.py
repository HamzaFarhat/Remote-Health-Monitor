from django.shortcuts import render
#from django import HttpResponse
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import VitalsSerializer
from .models import  Vitals
#import requests
import matplotlib.pyplot as plt
from io import StringIO
# import numpy as np




def createGraph(myList, name):
    
    x = []
    y = []
    for idx, val in enumerate(myList[0:30]):
        y.append(val)
        x.append(idx)
    fig = plt.figure()
    print(name,":", y)
    plt.plot(x, y)
    print(x)
    plt.ylabel(name)
    plt.xlabel("Time")
    titleName = name + " History"
    plt.title(titleName)

    imgData = StringIO()
    fig.savefig(imgData, format='svg')
    


    plt.clf()
    plt.cla()
    plt.close(fig)

    imgData.seek(0)

    data = imgData.getvalue()
    
    
    return data
    

def index(request):
    vitalList = Vitals.objects.all()
    recentVital = Vitals.objects.all().last()


    
    sys_list = [float(o.systolic) for o in vitalList]
    dia_list = [float(o.diastolic) for o in vitalList]
    hr_list = [float(o.heartRate) for o in vitalList]
    spo_list = [float(o.oxygenSaturation) for o in vitalList]

    sysGraph = createGraph(sys_list, "Systolic")
    diaGraph = createGraph(dia_list, "Diastolic")
    hrGraph = createGraph(hr_list, "Heart Rate");
    spoGraph = createGraph(spo_list, "Oxygen Saturation Levels")

    vitalList = vitalList[0:5]



    # tempGraph = createTempGraph(temp_list)
    # humidGraph = createHumidityGraph(temp_list)
   
    #, 'weather': weather, 'country':country, 'tempgraph': tempGraph, "humidgraph": humidGraph
    context = {'recentVital': recentVital, 'vitalList': vitalList,
               'sysGraph': sysGraph, 'diaGraph': diaGraph, 'hrGraph': hrGraph, 'spoGraph': spoGraph}
    return render(request, 'index.html', context=context)



class VitalsView(viewsets.ModelViewSet):
    serializer_class = VitalsSerializer
    queryset = Vitals.objects.all()

#most recent sys, dia, hr, spo2
#graph for each
