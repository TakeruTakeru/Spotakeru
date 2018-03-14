
from django.shortcuts import render, redirect
from .models import Basic_data
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .tracks import Spotakeru
from django.core.paginator import Paginator, InvalidPage
# Create your views here.
def post_list(request):
    posts = Basic_data.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    paginator = Paginator(posts, 5)

    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    try:
        fp = paginator.page(page)
    except (EmptyPage, InvalidPage):
        fp = paginate.page(paginator.num_pages)

    return render(request, "chat/index.html", {"posts": fp})

def post_detail(request, pk):
    post = get_object_or_404(Basic_data, pk=pk)
    return render(request, "chat/main.html", {"post": post})

def post_make(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, "chat/post.html", {"form": form})

def check_spotify(request):
    artist_name = request.GET.get('name')
    artist_name = str(artist_name)
    result = Spotakeru.search(artist_name)

    artist_list = []
    url_list = []
    for i in result["artists"]["items"]:
        artist_list.append(i["name"])
        url_list.append(i["external_urls"]["spotify"])

    image_list = []
    for i in result["artists"]["items"]:
        image_list.append[i["images"][0]["url"]]


    add_list = [k + ": " + v for k, v in zip(artist_list, url_list)]
    artist_dict = {
        "names": add_list,
        }

    return render(request, 'chat/check_spotify.html', artist_dict)
