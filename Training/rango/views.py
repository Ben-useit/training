# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

def index(request):
    return HttpResponse("Ganz alleine geschafft.")

def index2(request):
    return HttpResponse('Jetzt bin auf er rango seite.')