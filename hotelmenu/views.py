from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import models
from .models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

import json


def index(request):
    return HttpResponse("Hello, world. You're at the Hotel Menu.")


def sections_menu(request):
    # Endpoint is used for to display all the records
    result = items.objects.all().select_related('section_id')
    data = serialize("json", result)
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def insert_menu(request):
    # Endpoint for insert and delete the records
    if request.method == 'POST':
        body = json.loads(request.body)
        if body.get('category') == 'Section':
            a = sections(name=body['name'], descriptions=body['description'])
            a.save()

        elif body.get('category') == 'Item':
            a = items(name=body['name'], descriptions=body['description'], price=body['price'],
                      section_id=body['section_id'])
            a.save()
        elif body.get('category') == 'modifiers':
            a = modifiers(descriptions=body['description'], items_id=body['items_id'])
            a.save()
        return HttpResponse("successfully inserted record")
    elif request.method == 'DELETE':
        body = json.loads(request.body)
        ID = int(body['id'])
        if body.get('category') == 'Section':
            a = sections.objects.filter(Id=ID).delete()
        elif body.get('category') == 'Item':
            a = items.objects.filter(Id=ID).delete()
        elif body.get('category') == 'modifiers':
            a = modifiers.objects.filter(Id=ID).delete()
        return HttpResponse("successfully Deleted record !")

    else:
        return HttpResponse("Method Not Allowed!")


@csrf_exempt
def item_mapping(request):
    # Endpoint for mapping the items and modifiers
    if request.method == 'POST':
        body = json.loads(request.body)
        ID = int(body['id'])
        if body.get('category') == 'Item':
            a = items.objects.filter(Id=body['id']).update(section_id=body['items_id'])
            print(a)
        elif body.get('category') == 'modifiers':
            a = modifiers.objects.filter(Id=body['id']).update(items_id=body['items_id'])
        return HttpResponse("successfully Deleted record !")
    else:
        return HttpResponse("Method Not Allowed!")
