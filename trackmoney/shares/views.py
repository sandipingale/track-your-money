from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ShareForm
from django.views.generic import ListView
from .models import Share
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum


# Create your views here.

def index(request):
    return HttpResponse("This is test")


class ShareProcess(View):
    template_name = "shares/share_process.html"
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = ShareForm()
        return render(request, self.template_name, {"form": form})

    @method_decorator(login_required)
    def post(self, request,  *args, **kwargs):
        form = ShareForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return render(request, "shares/share_list.html", {"share_list": Share.objects.filter(owner=self.request.user)})
        else:
            return render(request, self.template_name, {"form": form, "error": "some problem with form"})

@method_decorator(login_required, name="dispatch")        
class ShareListView(ListView):
    context_object_name = "share_list"
    template_name = "shares/share_list.html"

    def get_queryset(self):
        user = self.request.user
        return Share.objects.filter(owner=user).aggregate(Sum('txn_price'))