from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from plotly.utils import PlotlyJSONEncoder
import json
import plotly.graph_objs as go
import pandas as pd
from random import random

graph_main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.01,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":10, "r":10, "t":30, "b":10},
    "title": dict(x=0.04, y=0.94, yref='container',
             xanchor='left', yanchor='top'),
    'plot_bgcolor':'rgba(0,0,0,0)'
}


@login_required
def home_dash(request):
    context = {'data_ini': request.GET.get('data_ini','2024-04-01'),
                 'data_fim': request.GET.get('data_fim','2024-05-05')}
    
    return render(request, 'dash/index.html', context)


def graph_view(request):
    body =json.loads(request.body)

    start_date = body['data_ini']
    end_date = body['data_fim']
    
    datas = pd.date_range(start_date, end_date, freq='D')

    y_1 = [random() for i in range(datas.shape[0])]
    y_2 = [random() for i in range(datas.shape[0])]

    fig1 = go.Figure(
        go.Scatter(x=datas, y=y_1, mode='lines+markers')
    )

    fig1.update_layout(graph_main_config, autosize=True, separators=',', title='grafico1')

    fig2 = go.Figure(
        go.Scatter(x=datas, y=y_2, mode='lines+markers')
    )

    fig2.update_layout(graph_main_config,  separators=',', title='grafico2')

    graphs = [fig1, fig2]
    graphs_contex = json.dumps(graphs, cls=PlotlyJSONEncoder)

    return JsonResponse(graphs_contex, safe=False)