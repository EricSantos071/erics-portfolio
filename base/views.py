from django.shortcuts import render  #Html render
from .models import Experience, Bio  # You must import your models!

def home(request):
    # 1. Fetch data from the database
    # .first() gets the only bio entry; .all() gets every experience
    bio = Bio.objects.first() 
    experiences = Experience.objects.all().order_by('-created_at')

    # 2. Pack the data into a dictionary (the 'context')
    context = {
        'bio': bio, 
        'experiences': experiences
    }

    # 3. Send the plate (html) AND the food (context) to the browser, waiter analogy
    return render(request, 'base/home.html', context)