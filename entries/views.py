from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm



def index(request):
    entries = Entry.objects.all()
   # fo = EntryForm.objects.all('id')
    fo = EntryForm()

    context = {'entries' : entries, 'fo':fo }

    return render(request, 'entries/inde.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inde')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)