from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404, HttpResponse
from .models import Blog
import time
import os
import pandas as pd
global table1

global ind
ind = 0;
# Create your views here.
time.localtime(time.time())
def start(request):
    blogs = Blog.objects
    
    global table1
    table1 = pd.DataFrame(
    {
        'data': [],
        'item': [],
        'price': [],
    })
    print(table1)
    return render(request, 'start.html', {'blogs': blogs})

def home(request):
    blogs = Blog.objects
    return render(request, 'pos.html', {'blogs': blogs})

def download(request):
    blogs = Blog.objects
    table1.to_excel('table1.xlsx')
    #with pd.ExcelWriter('inventors.xlsx') as writer:
        #inventors[inventors.name == 'Nikola Tesla'].to_excel(writer, sheet_name='Nikola Tesla')
        #inventors[inventors.name == 'Thomas Edison'].to_excel(writer, sheet_name='Thomas Edison')
        #inventors[inventors.name == 'Henry Ford'].to_excel(writer, sheet_name='Henry Ford')   
    if os.path.exists('table1.xlsx') :
        with open('table1.xlsx', 'rb') as fh :
            responese = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            responese['Content-Disposition'] = 'inline; filename = ' + os.path.basename("table1.xlsx")
            return responese
    raise Http404

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/pos/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/pos/detail/' + str(blog.id))

    else:
        return render(request, 'update.html')

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/pos/')

def m1(request) :
    global ind
    blog = Blog()
    blog.title = "[Table1] 호출"
    blog.body = "호출"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    table1.loc[ind] = [time.strftime('%Y-%m-%d', time.localtime(time.time())), "호출", "0"]
    ind += 1
    print(table1)
    return render(request, 'm1.html')

def m2(request) :
    global ind
    blog = Blog()
    blog.title = "[Table1] 소주"
    blog.body = "소주"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    table1.loc[ind] = [time.strftime('%Y-%m-%d', time.localtime(time.time())), "소주", "3000"]
    ind += 1
    print(table1)
    return render(request, 'm2.html')

def m3(request) :
    global ind
    blog = Blog()
    blog.title = "[Table1] 병맥주"
    blog.body = "병맥주"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    table1.loc[ind] = [time.strftime('%Y-%m-%d', time.localtime(time.time())), "병맥주", "3000"]
    ind += 1
    print(table1)
    return render(request, 'm3.html')

def m4(request) :
    global ind
    blog = Blog()
    blog.title = "[Table1] 메뉴판"
    blog.body = "메뉴판"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    table1.loc[ind] = [time.strftime('%Y-%m-%d', time.localtime(time.time())), "메뉴판", "0"]
    ind += 1
    print(table1)
    return render(request, 'm4.html')

def m5(request) :
    global ind
    blog = Blog()
    blog.title = "[Table1] 라면"
    blog.body = "라면"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    table1.loc[ind] = [time.strftime('%Y-%m-%d', time.localtime(time.time())), "라면", "2000"]
    ind += 1
    print(table1)
    return render(request, 'm5.html')