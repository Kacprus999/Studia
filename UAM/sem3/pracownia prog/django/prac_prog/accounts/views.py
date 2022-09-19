from django.shortcuts import render
from django.core.paginator import Paginator
# accounts/views.py
from .models import Member
from .forms import MemberForm

def home(request):
    all_members = Member.objects.all()
    
    p = Paginator(all_members, 5)
    
    print(' Liczba stron ')
    print(p.num_pages)
    
    page_num = request.GET.get('page', 1)
    
    try:
        page= p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    
    return render(request, 'home.html', {'all':page})
    
def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html',{})
    else:
        return render(request, 'join.html',{})