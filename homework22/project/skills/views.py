from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def home(request):
    link_list = ['Skills','Education']
    contact_list = {'Vk' : 'https://vk.com/id159525701', 
                    'Instagram': 'https://www.instagram.com/kotiki_meow/',
                    'Github' : 'https://github.com/MikhailPrizba',
                    
                    }
    
    return render(request, 'home.html',{"link_list": link_list , "contact_list" : contact_list.items()})

def skills(request):
    return render(request, 'skills.html')



def education(request):
    return render(request, 'education.html')
