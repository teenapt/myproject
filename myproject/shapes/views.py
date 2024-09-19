from django.shortcuts import render

# Create your views here.
# shapes/views.py

# shapes/views.py

from django.http import HttpResponse
from .rectangle import Rectangle

def rectangle_view(request):
    my_rectangle = Rectangle(length=10, width=5)
    output = f"Rectangle instance: {my_rectangle}<br>Iterating over rectangle:<br>"
    for dimension in my_rectangle:
        output += f"{dimension}<br>"
    return HttpResponse(output)
