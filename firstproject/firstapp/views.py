from django.shortcuts import render
from firstapp.forms import NewBookForm
from firstapp import models
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def newBook(request):
    form=NewBookForm()
    res=render(request,'new_book.html',{'form':form})
    return res

def add(request):
    if request.method == 'POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.author=form.data['author']
        book.save()
    s="Record Stored<br><a href='/view-books'>View All Books </a>"
    return HttpResponse(s)

def viewBook(request):
    books=models.Book.objects.all()
    res=render(request,'view_book.html',{'books':books})
    return res

def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('view-book')

def editBook(request):
    book = models.Book.objects.get(id=request.GET['bookid'])
    # fields={'title':book.title,'author':book.author}
    form=NewBookForm()
    res=render(request,'edit_book.html',{'form':form,'book':book})
    return res

def edit(request):
    if request.method=="POST":
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.author=form.data['author']
        book.save()
        return HttpResponseRedirect('view-book')
