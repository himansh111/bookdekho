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
from finalcredit.settings import MEDIA_ROOT
from django.template import RequestContext
from users.form import UserForm, UserProfileForm
from django.shortcuts import render_to_response
from django.http import HttpResponse
from course.models import Course
from category.models import Category
from booklist.models import Booklist
from novel.models import Novel


def home(request):
    title = Course.objects.all()
    return render(request, 'index.html', {'title': title})
@login_required
def books(request,id):
    title = Category.objects.filter(category=id)
    return render(request, 'books.html', {'title': title})
def book(request):
    title = Category.objects.all()
    return render(request, 'books.html', {'title': title})
def booklist(request,id):
    title = Booklist.objects.filter(category=id)
    return render(request, 'bookslist.html', {'title': title})


def novels(request):
    title = Novel.objects.all()
    return render(request, 'novels.html', {'title': title})
def contact(request):
    title = Category.objects.all()
    return render(request, 'contact.html', {'title': title})
def bookslist(request,id):
    title = Booklist.objects.filter(add=id)
    return render(request, 'bookslist.html', {'title': title})


def profile(request):
    title = Novel.objects.all()
    return render(request, 'novels.html', {'title': title})

def auth_view(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
            uform = UserForm(data=request.POST)
            pform = UserProfileForm(data=request.POST)
            # is_private = request.POST.get('is_private', False)
            if uform.is_valid() and pform.is_valid():
                user = uform.save()
                # form brings back a plain text string, not an encrypted password
                pw = user.password
                # thus we need to use set password to encrypt the password string
                user.set_password(pw)
                user.save()
                profile = pform.save(commit=False)
                profile.user = user
                profile.save()
                save_file(request.FILES['picture'])
                registered = True
            else:
                print uform.errors, pform.errors
        else:
            uform = UserForm()
            pform = UserProfileForm()

        return render_to_response('signup.html', {'uform': uform, 'pform': pform, 'registered': registered}, context)


def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("/profile/")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
        else:
            # Return an 'invalid login' error message.
            print  "invalid login details " + username + " " + password
            return render_to_response('login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect('/home/')