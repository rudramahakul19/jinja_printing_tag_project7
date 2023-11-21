from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This data is our assumption'
    Rudra="Heyy i'am Rudra Prakash Mahakul"
    d={'assumption':data,'Name':Rudra}

    return render(request,'data_render.html',context=d)