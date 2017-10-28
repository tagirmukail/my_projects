# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from .models import *
from .load import run
import csv
from .render_tile import render_tile

# Create your views here.

def index(request):
    """представление для отображения карты."""
    # подключаем модель.
    objects = GeoBorder.objects.all()

    # Выгрузка данных из shape файла, если не загружались в бд.
    if len(objects) == 0:
        run()
    path_to_tile = 'static/tiles/0/0/0.png'
    try:
        if open('worldmap/static/tiles/0/0/0.png', 'r'): pass
    except:
        render_tile()

    return render(request, 'worldmap/index.html')
