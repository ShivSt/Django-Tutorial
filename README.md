# Some basic references

## models :

*models are in simple term a tables for your data. So, you need seperate model class for seperate tables. These tables are wriitn in the DB you assigned in project's setting.py.*

Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

## admin :

Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models.

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.

## apps :

*Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.*

Adding apps from external projects:
- download istall via pip or other installer
- install into your project by adding adding appconfig in list of installed_apps in project's setting.py
- Use its feature in your models, admin, app, views wherever applicable

## views and templates :

views.py in our app is the place where we write the feature code for every page/link. It will consist of several function/method which are defined for seperate pages(generally). It will transmit the model data to template (your html page)

templates are html pages which will be displayed by the browser. Here your design your page look and feel. Django generaly look for the templates in 'your app'/templates directory. So place them there. Since other apps in your project can have same template name. So, good practice is to create a folder named after your project name and place your templates there

## styling with css :

All the css are to be imported in templates. Django generaly look for the css in 'your app'/static directory. So place them there. Since other apps in your project can have same css name. So, better use "static/app-name/css-name"

We can use material design css from materializecss.com or other free site
it is free and easy to configure.

we can just copy element from there and edit the values with our contents eg. nav bar, cards, tables etc. and modify its css by changing the scss (sass) file and compiling it to css file and adding it to our static/css/ folder in app folder.

## user registration :

We need to add an template for user registration page and there use html form element.

In views add an function for the the register and
use django authenticator and UserCreationForm from django
form is a post request so after successful registration redirect user to home page (or where intended).

## user login and logout :

- For logout we dont need an template.
we only need to write a function in view for logout request and refrence url
in urls.py is "/logout"
We will also redirect user to homepage

- For login we can create a template with form element with django AuthenticationForm defined in views.py which require user to input username and password we then authenticate and log user in and redirects to homepage

## messages :

To inform user whats going on we use messages from django.contrib
we can display messages using M.Toast('meesage') inside script block.
*Here M.toast() is a js function defined in materializecss.com's refrenced script*

## include :
- It is used to include seperate html block/code in one html.
- It helps in cleaning long html for one page by using seperate html for different element eg.
{% include "mainApp/includes/navbar.html" % }
it will place all the html elements in navbar.html within calling template
at specified place

## Linking models withForeign Keys :

- Organizing your database by refrencing different tables viz. creating category, series, and main table they are linked by Foreign key.
- Then we will use a single_slug (one function) to point to all different categories and series
instead of different functions for them in views.py
- It is the most importpart for organizing data of your application in a logical way. can be complex at time as well