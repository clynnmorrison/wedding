from django.http import HttpResponse
import urllib
from django.shortcuts import render, redirect
import urllib2
from django.views.decorators.csrf import csrf_exempt
from wedding import forms
from wedding.models import Rsvp
from django.forms.models import modelformset_factory

def render_wedding_woo(request):
    req = urllib2.Request('http://candwedding.weddingwoo.com'+request.path_info)
    try:
        response = urllib2.urlopen(req)
        the_page = response.read().replace("http://candwedding.weddingwoo.com", "")
        return HttpResponse(the_page)
    except urllib2.HTTPError, e:
        return redirect("/")

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

    #req.add_header("Host", "candwedding.weddingwoo.com")
    #req.add_header("Origin", "http://candwedding.weddingwoo.com")
    #req.add_header("Referer", "http://candwedding.weddingwoo.com/song-requests")

    #req.add_header("X-CSRF-Token", "iyGuiCqbEm9ACnZ4knYVFPtTEiOIACu5lQUfR2z7gnFxrmOdI1eQr8WE66kkr3w26iWPY8vXPqX/nzusqrD0Qg==")
    req.add_header("X-Requested-With", "XMLHttpRequest")

    response = urllib2.urlopen(req)
    the_page = response.read()
    return HttpResponse(the_page,content_type='text/javascript; charset=utf-8')

def rsvp(request):
    RsvpFormset = modelformset_factory(Rsvp, form=forms.RsvpForm, extra=0)
    success_rsvp = False;
    if request.POST:
        formset = RsvpFormset(request.POST, queryset=request.user.rsvp_set.all())
        if formset.is_valid():
            formset.save()
        user_profile_form = forms.UserProfileForm(request.POST, instance=request.user.userprofile_set.all()[0],
                                                  prefix="user_profile_form")
        if user_profile_form.is_valid():
            user_profile_form.save()
        success_rsvp = True;
    rsvp_formset = RsvpFormset(queryset=request.user.rsvp_set.all())
    user_profile_form = forms.UserProfileForm(instance=request.user.userprofile_set.all()[0],
                                              prefix="user_profile_form")

    return render(request, 'wedding/rsvp.html', {'rsvp_formset': rsvp_formset,
                                                 'user_profile_form': user_profile_form,
                                                 'success_rsvp': success_rsvp})
