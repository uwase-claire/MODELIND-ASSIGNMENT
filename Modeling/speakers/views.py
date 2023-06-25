from django.shortcuts import render, get_object_or_404, redirect
from .models import Speaker
from .forms import SpeakerForm
from django.http import HttpResponse
def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('speakers:list')
    else:
        form = SpeakerForm()
    return render(request, 'speakers/create_speaker.html', {'form': form})

def update_speaker(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        if form.is_valid():
            form.save()
            return redirect('speakers:list')
    else:
        form = SpeakerForm(instance=speaker)
    return render(request, 'speakers/update_speaker.html', {'form': form, 'speaker': speaker})

def delete_speaker(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    if request.method == 'POST':
        speaker.delete()
        return redirect('speakers:list')
    return render(request, 'speakers/delete_speaker.html', {'speaker': speaker})

def speaker_details(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    return render(request, 'speakers/speaker_details.html', {'speaker': speaker})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})









#conference views
from django.shortcuts import render, get_object_or_404, redirect
from conferences.models import Conference
from conferences.forms import ConferenceForm

def create_conference(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conferences:list')
    else:
        form = ConferenceForm()
    return render(request, 'conferences/create_conference.html', {'form': form})

def update_conference(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            form.save()
            return redirect('conferences:list')
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'conferences/update_conference.html', {'form': form, 'conference': conference})

def delete_conference(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    if request.method == 'POST':
        conference.delete()
        return redirect('conferences:list')
    return render(request, 'conferences/delete_conference.html', {'conference': conference})

def conference_details(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conferences/conference_details.html', {'conference': conference})

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conferences/conference_list.html', {'conferences': conferences})
