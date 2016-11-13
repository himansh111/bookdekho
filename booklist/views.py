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
from booklist.models import Booklist
def bookslist(request,id):
    title = Booklist.objects.filter(add=id)
    return render(request, 'bookslist.html', {'title': title})

