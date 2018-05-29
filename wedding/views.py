from django.http import HttpResponse
import urllib

import urllib2
from django.views.decorators.csrf import csrf_exempt

def render_wedding_woo(request):
    req = urllib2.Request('http://candwedding.weddingwoo.com'+request.path_info)
    response = urllib2.urlopen(req)
    the_page = response.read().replace("http://candwedding.weddingwoo.com", "")
    return HttpResponse(the_page)

def suggestions(request):
    args = {"term": request.GET.get("term")}
    url = 'http://candwedding.weddingwoo.com' + request.path_info+"?"+urllib.urlencode(args)
    req = urllib2.Request(url)
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    response = urllib2.urlopen(req)
    the_page = response.read()
    return HttpResponse(the_page)


@csrf_exempt
def suggest(request):
    param_str = ""
    args =  dict(request.POST)
    del(args["utf8"])
    for key, value in args.items():
        if isinstance(value, list):
            param_str += "{}={}&".format(key, value[0])
        else:
            param_str += "{}={}&".format(key, value)

    url = 'http://candwedding.weddingwoo.com/suggest'
    req = urllib2.Request(url, param_str)

    req.add_header("Host", "candwedding.weddingwoo.com")
    req.add_header("Origin", "http://candwedding.weddingwoo.com")
    req.add_header("Referer", "http://candwedding.weddingwoo.com/song-requests")

    req.add_header("X-CSRF-Token", "iyGuiCqbEm9ACnZ4knYVFPtTEiOIACu5lQUfR2z7gnFxrmOdI1eQr8WE66kkr3w26iWPY8vXPqX/nzusqrD0Qg==")
    req.add_header("X-Requested-With", "XMLHttpRequest")

    response = urllib2.urlopen(req)
    the_page = response.read()
    return HttpResponse(the_page,content_type='text/javascript; charset=utf-8')

