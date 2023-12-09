from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Details

# Create your views here.


def home(request):
    dest1=Details()
    dest1.name='pramod'
    return render(request,'home.html')

def details_form(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        mobile = request.POST.get('mobile')
        colour = request.POST.get('colour')
        dob = request.POST.get('dob')
        file=request.POST.get('file')

        # Create a new Details object and save it to the database
        details = Details.objects.create(
            name=name,
            desc=desc,
            mobile_number=mobile,
            colour=colour,
            dob=dob,
            img=file
        )
        details.save()

        return redirect('home')

    return render(request, 'details.html')