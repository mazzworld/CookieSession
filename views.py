from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponse("index")


def post_page(request):
    return render(request,'PostPage.html')


def do_post_page(request):
    print(request.POST)
    return HttpResponse('请求成功，获取参数')


def get_content(request):
    return redirect(reverse('app:index'))


def home(request):

    # username = request.COOKIES.get("user")

    username = request.session.get("user")

    return render(request, "home.html",context={"username":username})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")

        response = HttpResponse("登陆成功")

        # response.set_cookie("user" , username)
        request.session['user'] = username

        return response


def logout(request):

    response = HttpResponse("删除成功")

    # response.delete_cookie("user")
    # response.delete_cookie("sessionid")

    # del  request.session['user']
    #同时删除Ｃｏｏｋｉｅ和Ｓｅｓｓｉｏｎ
    request.session.flush()

    return response