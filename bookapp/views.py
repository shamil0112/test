from django.shortcuts import render,redirect,get_list_or_404
from.models import *
# Create your views here.


def index(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        description = request.POST['description']
        price = request.POST['price']
        published_date = request.POST['date']
        
        book = BooksForm(title=title, author=author,genre=genre, description=description, price=price, published_date=published_date )
        
        book.save()
        return redirect ('/')
    
    book_list = BooksForm.objects.all()
        
    return render(request,"index.html",{"book_list":book_list})

def delete_(request,id):
    dele = BooksForm.objects.get(id=id)
    dele.delete()
    return redirect('/')

def edit_(request,pk):
    edit__=get_list_or_404(BooksForm, pk=pk)
    if request.method == 'POST':
        edit__.title = request.POST['title']
        edit__.athor = request.POST['author']
        edit__.genre = request.POST['title']
        edit__.description = request.POST['author']
        edit__.price = request.POST['title']
        edit__.published_date = request.POST['author']
        edit__.save()
        return redirect('/')
    return render(request,"edit.html",{'edit__':edit__})