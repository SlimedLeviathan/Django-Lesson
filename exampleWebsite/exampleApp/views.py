from django.shortcuts import render

# Create your views here.

numberOfVisits = 0
def page(request):
    global numberOfVisits
    # First we NEED this parameter here, it doesn't need to be called request but it relates to the user and the url

    # To send something back we return an HttpRepsonse with a string in it that gets displayed on the page for the user
    numberOfVisits += 1

    context = {'visits':numberOfVisits}

    return render(request, 'main.html', context = context)