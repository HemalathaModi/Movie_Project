from django.shortcuts import render, redirect, get_object_or_404
from .models import Movieinfo
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url = 'login')
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('list')
    else:
        form = MovieForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url = 'login')
def list(request):
    query = request.GET.get('q')
    movies = Movieinfo.objects.all()

    if query:
        movies = movies.filter(title__icontains = query)

    if movies.exists():
        return render(request, 'list.html', {'movies': movies})
    
    else:
        return redirect('create')
    
@login_required(login_url = 'login')   
def favorites(request):
    query = request.GET.get('q')
    movies = Movieinfo.objects.filter(user=request.user)

    if query:
        movies = movies.filter(title__icontains = query)

    if movies.exists():
        return render(request, 'favorites.html', {'movies': movies})
    
    else:
        return redirect('create')

@login_required
def edit(request, pk):
    movie = get_object_or_404(Movieinfo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('favorites')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form, 'movie':movie})

@login_required
def delete(request, pk):
    movie = get_object_or_404(Movieinfo, pk= pk, user= request.user)
    if request.method == 'POST':
        movie.delete()
        return redirect('favorites')
    return render(request, 'delete.html', {'movie':movie})