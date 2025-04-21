from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all().order_by("-created_at")
    return render(request, "events/event_list.html", {"events": events})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "events/event_detail.html", {"event": event})

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.added_by = request.user
            event.save()
            return redirect("event-detail", id=event.id)
    else:
        form = EventForm()
    return render(request, "events/event_form.html", {"form": form})

@login_required
def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.user != event.author:
        return HttpResponseForbidden("You are not allowed to edit this event.")

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event-detail", id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, "events/event_form.html", {"form": form})

@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.user != event.author:
        return HttpResponseForbidden("You are not allowed to delete this event.")

    if request.method == "POST":
        event.delete()
        return redirect("event-list")
    return render(request, "events/event_confirm_delete.html", {"event": event})
