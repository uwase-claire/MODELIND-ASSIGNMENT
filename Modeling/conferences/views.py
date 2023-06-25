from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference
from .forms import ConferenceForm
 
def create_conference(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conferences:list')
    else:
        form = ConferenceForm()
    return render(request, 'create_conference.html', {'form': form})

def update_conference(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            form.save()
            return redirect('conferences:list')
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'update_conference.html', {'form': form, 'conference': conference})

def delete_conference(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        conference.delete()
        return redirect('conferences:list')
    return render(request, 'delete_conference.html', {'conference': conference})

def conference_details(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference_details.html', {'conference': conference})

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})
