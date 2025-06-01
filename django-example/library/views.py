from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect("book_list")
    return render(request, "library/add_book.html")