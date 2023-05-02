from django.shortcuts import render


posts = [
    {
        "author": "OsimFavour",
        "title": "Tech Blog Post 1",
        "content": "First Post Content",
        "date_posted": "May 1, 2023"
    },
{
        "author": "John Doe",
        "title": "Tech Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "May 1, 2023"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "techblog/home.html", context)


def about(request):
    return render(request, "techblog/about.html", {"title": "About"})
