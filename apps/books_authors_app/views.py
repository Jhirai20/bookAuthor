from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book




def index(request):
    context = { "books" : Book.objects.all()}
    return render(request,'books_authors_app/index.html', context)

def addBook(request):
    if request.method =="POST":
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc']) # need to make sure its capital POST!
    return redirect("/")

def books(request, id):
    context = { 
        'authors' :Book.objects.get(id=id).author.all(),
        "book" : Book.objects.get(id=id),
        'allAuthors':Author.objects.all()
    }
    return render(request,'books_authors_app/book.html', context)

def addAuthorB(request, id,aid):
    if request.method =="POST":
        author= Author.objects.get(id=aid)
        book=Book.objects.get(id=id)
        book.authors.add(author)
    return redirect("/")