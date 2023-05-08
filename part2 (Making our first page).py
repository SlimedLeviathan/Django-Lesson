from django.shortcuts import HttpResponse
# This code is already inside of the views function, disregard everything above this comment

# Now that we have made the setup for our website, we need to make a page for it and have out python code handle and send information to and from a user

# Inside of the views function, we are going to make a function, name it whatever you want but we need a couple of things


#views.py
# Our Function (type this into your views function)
def page(request):
    # First we NEED this parameter here, it doesn't need to be called request but it relates to the user and the url

    # To send something back we return an HttpRepsonse with a string in it that gets displayed on the page for the user
    return HttpResponse('This page is working!!!!!')

# This is all the code we need behind a website to get it to send one hard coded string, but we still need to add this function to our urls.py file
#views.py


#urls.py
# inside our urls.py file inside the app folder, put this code into the file

from django.urls import path

from . import views

urlpatterns = [
    # This code looks for the url appName/ and if so it looks for our function and sends whatever is in the return function

    # Change this to the name of your function
    #               \/
    path('', views.page, name='page'),
]
#urls.py

# This will now actually work if you start the server using [manage.py runserver] and go to http://localhost:8000/appName/ in your browser
# If you want to try it with the example site in the files, you will have to use ecampleApp/ instead of appName

# After the page starts, you will see the text you put into the HTTP Response inside the site

# To make one last change to the pag we will make the page change based on how many people have visited (or reloaded) the site since the last restart

# Inside of the views.py file, make a variable that represents the number of visits

# Make the variable go up by one for each time someone runs the function page()

# And finally, change the text inside to show the variable inside of the HTTPResponse (use f-strings)

# In future parts, we will use HTML instead of simple text, and add more functionality to our site