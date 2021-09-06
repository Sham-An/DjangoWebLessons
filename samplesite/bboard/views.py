#from django.http import HttpResponse
#from django.template import loader

#def index(request):
#    return HttpResponse('Здесь будет выведен список объявлений.')

from django.shortcuts import render
from .models import Bb
from .models import Rubric

def index(request):
    #s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title +'\r\n'+ bb.content + '\r\n\r\n'
    # return  HttpResponse(s, content_type='text/plain; charset=utf8')

    # template = loader.get_template('bboard/index.html') #Str43
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))

    #bbs = Bb.objects.order_by('-published')#all()
    #return render(request, 'bboard/index.html', {'bbs': bbs})

    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.object.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

#from django.shortcuts import render

# Create your views here.
