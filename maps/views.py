from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Stage, Blueprint, Level

# Create your views here.


def RowToArray(row):
    res = row.split(',')
    res = map(int, res)
    res = list(res)
    return res

def WallToMatrix(wall):
    res = wall.split('\n')
    res = map(RowToArray, res)
    res = list(res)
    return res

def BlueprintToJson(blueprint):
    res = dict()
    res['vertical'] = WallToMatrix(blueprint.verticals)
    res['horizontal'] = WallToMatrix(blueprint.horizontals)
    res['size'] = {'cols': len(res['horizontal'][0]), 'rows': len(res['vertical'])}
    return res

@csrf_exempt
def blueprint(request, blueprint_id):
    target = get_object_or_404(Blueprint, pk=blueprint_id)
    return JsonResponse(BlueprintToJson(target), status=200)

@csrf_exempt
def level(request, level_id):
    target = get_object_or_404(Level, pk=level_id)
    actual = target.blueprint

    res = BlueprintToJson(actual)
    res['level'] = target.id
    res['title'] = target.title
    return JsonResponse(res, status=200)

@csrf_exempt
def stage(request, stage_id):
    target = get_object_or_404(Stage, pk=stage_id)
    levels = target.levels.values('levelno', 'id', 'title')
    levels = list(levels)
    return JsonResponse({'title': target.title, 'levels': levels})