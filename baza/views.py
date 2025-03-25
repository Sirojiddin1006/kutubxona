from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import News, Category


def news_list(request):
    news = News.objects.all().filter(status=News.Status.PUBLISHED)
    upnews = News.objects.all().filter(status=News.Status.Draft)
    context = {'news': news}
    return render(request, "news_list.html", context)


def news_detail(request, id):
    try:
        news = get_object_or_404(News, id=id, satatus=News.Status.PUBLISHED)
        context = {'news': news}
        return render(request, "news_detail.html", context)
    except:
        return HttpResponse("Error")


def homePageView(request):
    categories = Category.objects.all()
    news_list = News.objects.all().filter(status=News.Status.PUBLISHED).order_by('pulish_time')[:4]
    # print(news_list)
    mahalliy_news = News.objects.filter(category__name='Mahalliy').filter(status=News.Status.PUBLISHED)

    context = {
        'news_list': news_list,
        'categories': categories,
        'mahalliy_news': mahalliy_news, }
    return render(request, "index.html", context)


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Ma'lumotlariz saqlandi")
    context = {
        'form': form

    }
    return render(request, "contact.html", context)


def single(request, pk):
    news = get_object_or_404(News, id=pk)
    context = {'news': news}
    return render(request, 'single_page.html', context)


def xato(request):
    return render(request, '404.html')


def savol(request):
    return render(request, 'sorov.html')


def namerequest(request):
    name = request.GET.get('name')
    context = {
        'name': name

    }
    return render(request, 'sorov.html', context)
