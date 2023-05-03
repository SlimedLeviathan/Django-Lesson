# Django is a module in python that allows programmers to create websites using python

# This lesson will be focussed on downloading and getting django and our workspace set up on your system

# I'm going to assume that python is already installed on your computer
# to install django type either 

# py -m pip install django

# or

# pip install django


# To make sure that you have django installed properly type 

# py -m django --version


# If you get a response, you have installed django


# Now we need to set up our website, which is pretty simple since django has commands to make it for you

# to set up our website we'll type in this simple code into the terminal

#         change this if you want\/
# py -m django startproject siteName

# This added a fair bit pf files to your computer, so lets go over them quickly

# The first folder you'll see will be the name you put in for the command, in my case siteName, this folder contains all of your websites files

# The next couple of files you'll see is manage.py (we don't really mess with this) and another folder with the name you input

# inside of that file there are a couple more python files, including __init__.py, settings.py, urls.py, asgi.pu and wsgi.py

# __init__.py - Empty file that tells Python that this directory should be considered a Python package (we don't change this)
# settings.py - Has all of the settings for the server
# urls.py - Controls URLs for the site, gets changed when we run a later program (we don't change this tho)
# we really don't mess with asgi.py or wsgi.py

# using the command [py exampleWebsite\manage.py runserver] in this directory will start to run the server (you might need to change the directory in the command)
# going to http://127.0.0.1:8000/ on your computer will bring up a page that will tell you that the server is up and running and that you've done everything right from here

# we need to set up one last thing before we get started with our website

# run the command and make sure you are in the folder that contains all of the files for the website, or this won't work correctly

# again change this if you want\/
#     py manage.py startapp appName

# The folder should be inside the folder that contains all of the websites files, in the directory siteName\appName

# This created another set of files and we'll go over them as well:

# __init__.py - another file like the first __init__.py
# admin.py - where models get registered, or where we make models able to be interacted with by admins
# apps.py (ngl idk, haven't used it)
# models.py - where Models are made
    # Models are like classes but for django, they get stored in an sql file and are able to be configured with admin comands
# tests.py (ngl idk, haven't used it)
# views.py - inside of this file we program all of the python code behind every page of the website

# Now that the setup is complete we'll finish this part and go to part 2, where we'll be testing the website and setting up some basic pages for the website
# don't be afraid to go off the path I set down in the next couple of parts, use the steps i use to make whatever you want