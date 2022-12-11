from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserForm
from .forms import Form


# def gettutorial(request):
#     return render(request,'tutorial.html')

# # def postuser(request):
# #     name = request.POST.get('name',"Undefined")
# #     age = request.POST.get('age',1)
# #     lang = request.POST.getlist('languages',['python','',''])
    
# #     return HttpResponse(f"""<h2> Имя: {name} <br> Возраст: {age} </h2> <br> <div>Languages: {lang} </div>""")

# def form(request):
#     userform = UserForm()
#     return render(request,'tutorial.html', {'form':userform})

# def formsec(request):
#     if request.method == 'POST':
#         name = request.POST.get('name','Undefined')
#         age = request.POST.get('age',1)
#         return HttpResponse(f"""<h2> Имя: {name} <br> Возраст:{age} </h2>""")
#     else:
#         userform = UserForm()
#         return render(request,'tutorial.html',{'form':userform})

def index(request):
    if request.method == 'POST':
        print(dir(request.POST))
        return render(request, 'index.html', context={'data': str(list(request.POST.items()))})
    return render(request, 'index.html')


def form(req):
    return render(req, 'form.html', context={'form': Form})


def order(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render(request, 'order.html', context={
                'form': form,
                'data': request.POST
            })
    else:
        form = Form()
    
    return render(request, 'order.html', {'form': form})