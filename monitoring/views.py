from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import IARRecords
from django.core.paginator import Paginator
from .forms import IARRecordsForm

# Create your views here.
def index(request):
    recs = IARRecords.objects.all()

    paginator = Paginator(recs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)



    if request.method == 'POST':
        form = IARRecordsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('docsInventoryIndex')
        
    else:
        form = IARRecordsForm()

    return render(request, 'monitoring/index.html', {'form': form, 'recs': recs, 'page_obj':page_obj})