import re
from django.contrib.auth import authenticate, login
from django.shortcuts import render

class EnforceUserLogin(object):
    def process_request(self, request):
        username = request.GET.get("user", None)
        if not request.user.is_authenticated() or (username and username != request.user.username):
            if username:
                user = authenticate(username=username, password='password')
                if user:
                    login(request, user)
                    return

            return self.forbidden(request)

    def process_response(self, request, response):
        if request.user.is_anonymous():
            return response
        response.content = re.sub(r'href="(.*?)"', r'href="\g<1>?user='+request.user.username+'"', response.content.decode('utf-8').strip())
        response.content = response.content + "<script>element=document.getElementById('branding-footer');element.parentNode.removeChild(element);</script>"
        return response
    def forbidden(self, request):
        return render(request, "403.html")
