from django.shortcuts import render, redirect
from .models import VideoUrl
from urllib.parse import urlparse, parse_qs
from .forms import CreateVideoForm

# API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongsSerializers

# Create your views here.


@api_view(['GET'])
def api_get_song(request):
    songs = VideoUrl.objects.all()
    serializers = SongsSerializers(songs, many=True)

    return Response(serializers.data)


def home(request):

    if request.method == 'POST':
        form = CreateVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateVideoForm()

    def extract_video_id(url):
        query = urlparse(url)
        if query.hostname == 'youtu.be': return query.path[1:]
        if query.hostname in {'www.youtube.com', 'youtube.com'}:
            if query.path == '/watch': return parse_qs(query.query)['v'][0]
            if query.path[:7] == '/embed/': return query.path.split('/')[2]
            if query.path[:3] == '/v/': return query.path.split('/')[2]
        # fail?
        return None

    videos = VideoUrl.objects.all().order_by('-date')
    vid_downloaded = []
    vid_un_downloaded = []
    video_ids = []

    for video in videos:
        video_id = str(extract_video_id(video.url))
        if video.downloaded:
            vid_downloaded.append([video_id, video.name, video.downloaded, video.id])
        else:
            vid_un_downloaded.append([video_id, video.name, video.downloaded, video.id])

    video_ids.append([vid_un_downloaded, vid_downloaded])

    context = {
        "form": form,
        "video_ids": video_ids
    }
    return render(request, 'main/home.html', context)


def mark_downloaded(request, pk):
    video = VideoUrl.objects.get(id=pk)
    video.downloaded = True
    video.save()
    return redirect('home')


def mark_un_downloaded(request, pk):
    video = VideoUrl.objects.get(id=pk)
    video.downloaded = False
    video.save()
    return redirect('home')


def delete_video(request, pk):
    video = VideoUrl.objects.get(id=pk)
    video.delete()
    return redirect('home')
