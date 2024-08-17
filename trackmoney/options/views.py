from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def test_options(request):
    return HttpResponse("Thsi is your first page")

class Options(View):
    message = "This is first message"
    template_name = "options/index.html"
    def get(self, request, *args, **kwargs):
        print(args)
        return render(request, self.template_name, {})
