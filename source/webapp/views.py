import json
from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def expression(exp, data):
    answer = {}
    try:
        a = int(data['A'])
        b = int(data['B'])
        if exp == 'add':
            answer['answer'] = a + b
        elif exp == 'subtract':
            answer['answer'] = a - b
        elif exp == 'multiply':
            answer['answer'] = a * b
        elif exp == 'divide':
            answer['answer'] = a / b
    except Exception as e:
        print(e)
        answer['error'] = str(e)
        return JsonResponse(answer, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(answer)


def add_view(request, *args, **kwargs):
    data = json.loads(request.body)
    return expression('add', data)


def subtract_view(request, *args, **kwargs):
    data = json.loads(request.body)
    return expression('subtract', data)


def multiply_view(request, *args, **kwargs):
    data = json.loads(request.body)
    return expression('multiply', data)


def divide_view(request, *args, **kwargs):
    data = json.loads(request.body)
    return expression('divide', data)
