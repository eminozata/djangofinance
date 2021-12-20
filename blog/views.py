from django.shortcuts import render
from . import verilerim
# Create your views here.
import time



    

def post_list(request):
    veriler = verilerim.ne_durumdayım()
    kredi_verileri = verilerim.kredi_cuzdan()
    return render(request, 'blog/post_list.html', {"veriler": veriler,"kredi_verileri": kredi_verileri})