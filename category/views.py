#
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.template import RequestContext
# from django.core.paginator import Paginator, InvalidPage, EmptyPage
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.shortcuts import render, redirect
# from django.template.loader import get_template
## from django.template import Context
from django.contrib.auth.decorators import login_required
from category.models import Category
from booklist.models import Booklist
@login_required
def book(request,id):
    title = Category.objects.filter(id=id)
    return render(request, 'books.html', {'title': title})
@login_required
def books(request):
    title = Category.objects.all()
    return render(request, 'books.html', {'title': title})


def bookslist(request):
    title = Booklist.objects.all()
    return render(request, 'bookslist.html', {'title': title})