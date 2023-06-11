from django.shortcuts import render
finches = [
  {'name': 'cool bird', 'breed': 'finch', 'description': 'furry little demon', 'age': 3},
  {'name': 'other bird', 'breed': 'finch', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request): 
    return render(request, 'finches/index.html', {
        'finches': finches 
    })