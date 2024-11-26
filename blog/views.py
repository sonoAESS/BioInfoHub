from django.shortcuts import render, get_object_or_404
from .models import posts

# Create your views here.
def renderPosts(request):
    # Ordenar los posts por fecha, más reciente primero
    post = posts.objects.all().order_by('-date')  # Cambia 'date' por el nombre real del campo de fecha en tu modelo
    return render(request, 'posts.html', {
        'post': post
    })

def postDetail(request, post_id):
    post=get_object_or_404(posts,pk=post_id)
    return render(request,'postDetail.html',{
        'post':post
    })