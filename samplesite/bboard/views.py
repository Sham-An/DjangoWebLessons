#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    return HttpResponse('Здесь будет выведен список объявлений.')

from django.shortcuts import render
from .models import Bb

def index(request):
    #s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title +'\r\n'+ bb.content + '\r\n\r\n'
    # return  HttpResponse(s, content_type='text/plain; charset=utf8')

    # template = loader.get_template('bboard/index.html') #Str43
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))

    bbs = Bb.objects.order_by('-published')#all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

#from django.shortcuts import render

# Create your views here.
