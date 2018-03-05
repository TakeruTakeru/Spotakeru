from django.shortcuts import render, redirect
from .models import Basic_data
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.core.paginator import Paginator, InvalidPage

# Create your views here.
def post_list(request):
    posts = Basic_data.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    paginator = Paginator(posts, 5)

    try:
        page = int(request.GET.get("page", 1))
    except ValuError:
        page = 1
    try:
        posts= paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginate.page(paginator.num_pages)

    return render(request, "chat/index.html", {"posts": posts})

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
    pass
