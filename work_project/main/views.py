from django.shortcuts import render



def page(request, context=None):
  
    return render(request, 'main/page.html')




