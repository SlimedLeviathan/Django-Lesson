from django.shortcuts import HttpResponse, render
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


# Lets change the page so that the page changes based on how many people have visited (or reloaded) the site since the last restart

# Inside of the views.py file, make a variable that represents the number of visits

# Make the variable go up by one for each time someone runs the function page()

# And finally, change the text inside to show the variable inside of the HTTPResponse (use f-strings)

# Now, we will use HTML instead of a string to show the layout of our website

# Create a new folder called templates inside of our app folder

# We will need to go into the settings of the site in order to make sure our templates work corrctly

# Inside of the settings.py, change this part of the code:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

            # Set this to the directory of your templates folder
        'DIRS': ['siteName/appName/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Now that that should be good lets get to making the html

# make a file called page.html inside of your templates folder

# Inside the file, type <p>Type Whatever You Want Here!</p>

# Whatever is inside of the Ps will be shown on the website like it came from the HTTPResponse

# Now we need to change our views.py code.

# Inside of the code, change the return HTTPResponse code to:

render(request, 'page.html')

# This looks for our code in the templates folder (set in the settings file) and sends the data to the user

# To make out site change to data we will use later, lets make our site change again to show how many people have been on the site

# Make this code inside of the views file, over the render line

context = {'visits' : numOfVisits}

render(request, 'page.html', context = context)

# What this does is send the number of people who have visited the site to the html code, so we need to change that as well to show the code

# To get input from HTML, write this above our previous HTML code: {% if visits %}  this code checks for data under the name 'visits' and bc we set visits in the context, it gets the information

# Now we need to put this into our text, so to do that we need to write {{ visits }} inside of our <p></p> wherever you would like
# An example would be <p>Number of visits: {{ visits }}</p>

# And to end off the code, we write {% endif %} to end off the if statement

# This code should allow our website to run off of HTML code for the formatting.
# This is the end of this part of our django lesson, if you would like to change your website, changing the HTML code will put whatever you want onto the website, so now any HTML tags will be put into the website