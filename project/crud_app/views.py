from django.shortcuts import render,redirect
from .models import Event
from .forms import EventForm
from django.views import View


class Create_Event(View):
    def get(self, request):
        template_name = 'crud_app/create.html'
        form = EventForm()
        context = {'form':form}
        return render(request, template_name, context)

    def post(self, request):
        form = EventForm()
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('show_url')


class Show_Event(View):
    def get(self,request):
        template_name = 'crud_app/show.html'
        events = Event.objects.all()
        context = {'events':events}
        return render(request, template_name, context)

class Update_Event(View):
    def get(self,request,pk):
        template_name = 'crud_app/create.html'
        obj = Event.objects.get(id=pk)
        form = EventForm(instance=obj)
        context = {'form':form}
        return render(request, template_name, context)

    def post(self,request,pk):
        template_name = 'crud_app/create.html'
        obj = Event.objects.get(id=pk)
        form = EventForm(instance=obj)
        if request.method == "POST":
            form = EventForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('show_url')
        context = {'form': form}
        return render(request, template_name, context)


class Delete_Event(View):
    def get(self, request, pk):
        obj = Event.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        return render(request, template_name)

    def post(self, request, pk):
        obj = Event.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        if request.method == "POST":
            obj.delete()
            return redirect('show_url')
        return render(request, template_name)