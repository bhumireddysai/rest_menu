from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.db import models
from .models import sections, items, modifiers
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

import json


def index(request):
    return HttpResponse("Hello, world. You're at the Hotel Menu.")


def sections_menu(request):
    try:
        # Endpoint is used for to display all the records

        hotel_menu = []
        hotelmenu = {}
        sections = {}
        items = {}
        modifiers_dict = {}
        modifiers_list = []
        result = modifiers.objects.all()
        for book in result:
            # import pdb;pdb.set_trace();
            if (str(sections.get('id')) == str(book.items_id.section_id.Id)):
                modifiers_dict['id'] = str(book.Id)
                modifiers_dict['title'] = book.descriptions
                items['modifiers'].append(modifiers_dict)
            else:
                sections = {}
                sections['id'] = str(book.items_id.section_id.Id)
                sections['title'] = book.items_id.section_id.name
                items['id'] = str(book.items_id.Id)
                items['title'] = book.items_id.name
                modifiers_dict['id'] = str(book.Id)
                modifiers_dict['title'] = book.descriptions
                items['modifiers'] = [modifiers_dict]
                sections['items'] = items
                hotel_menu.append(sections)
        return HttpResponse(json.dumps(hotel_menu), content_type="application/json")
    except Exception as e:
        return HttpResponse("successfully inserted record :", str(e))


@csrf_exempt
def insert_menu(request):
    try:
        # Endpoint for insert and delete the records
        # import pdb;pdb.set_trace();
        if request.method == 'POST':
            body = json.loads(request.body)

            if body.get('category') == 'Section':
                a = sections(name=body['name'], descriptions=body['description'])
                a.save()

            elif body.get('category') == 'Item':
                section_obj = sections.objects.get(Id=body['section_id'])
                a = items(name=body['name'], descriptions=body['description'], price=body['price'],
                          section_id=section_obj)
                a.save()
            elif body.get('category') == 'modifiers':
                items_obj = items.objects.get(Id=body['items_id'])
                a = modifiers(descriptions=body['description'], items_id=items_obj)
                a.save()
            return HttpResponse("successfully inserted record !")
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
        elif request.method == 'GET':
            body = json.loads(request.body)
            ID = int(body['id'])
            if body.get('category') == 'Section':
                sections_obj = sections.objects.filter(Id=ID)
                serialized_data = json.loads(serialize('json', list(sections_obj)))
            elif body.get('category') == 'Item':
                items_obj = items.objects.filter(Id=ID)
                serialized_data = json.loads(serialize('json', list(items_obj)))
            elif body.get('category') == 'modifiers':
                modifiers_obj = modifiers.objects.filter(Id=ID)
                serialized_data = json.loads(serialize('json', list(modifiers_obj)))
            return JsonResponse({'data': serialized_data})
        else:
            return HttpResponse("Method Not Allowed!")
    except Exception as e:
        return HttpResponse("Exception CRUD operations! :", str(e))


@csrf_exempt
def item_mapping(request):
    try:
        # Endpoint for mapping the items and modifiers
        if request.method == 'POST':
            body = json.loads(request.body)
            ID = int(body['id'])
            if body.get('category') == 'Item':
                a = items.objects.filter(Id=body['id']).update(section_id=int(body['sections_id']))
                print(a)
            elif body.get('category') == 'modifiers':
                a = modifiers.objects.filter(Id=body['id']).update(items_id=int(body['items_id']))
            return HttpResponse("successfully Deleted record !")
        else:
            return HttpResponse("Method Not Allowed!")
    except Exception as e:
        return HttpResponse("successfully inserted record :", str(e))
