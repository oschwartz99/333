from django.shortcuts import render

posts = [
    {
        'author': 'Ollie',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 24, 2019'
    },
    {
        'author': 'Seb',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 25, 2019'
    }
]


# Traffic to home page
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# Traffic to about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})