import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from PantryPal_app.run_query import run_query
from PantryPal_app.forms import UserForm
from PantryPal_app.models import Query
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    result_list = []

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('PantryPal_app/index.html', {'result_list': result_list}, context)

def search(request):
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    result_list = []

    if request.method == 'POST':
        search_terms = request.POST['query'].strip()

        if not request.user.is_authenticated():
            render_to_response('PantryPal_app/search.html', {'result_list': result_list}, context)

        # converstion to seconds
        # handles empty max_time input
        if request.POST['time']:
            max_time = str(int(request.POST['time']) * 60)
        else:
            max_time = ''

        # Page number they wish to return
        offset = int(request.POST['page'])

        # Run our Yummly function to get the results list!
        result_list = run_query(search_terms, max_time, offset)

        # If user is authenticated and their query returned results
        if  result_list:
            q = Query(id = Query.objects.latest('id').id + 1,
                      user = request.user.username,
                      query = search_terms)
            q.save()

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('PantryPal_app/search.html', {'result_list': result_list}, context)

# def recipes(request):
#     context = RequestContext(request)

#     return render_to_response('PantryPal_app/recipes.html', context)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Grabs information from form
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Hash password and update user object
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            # Login User after registration
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

        # Invalid form or forms
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'PantryPal_app/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        login(request, user)

        # If we have a User object, the details are correct.
        # If None, no user with matching credentials was found.
        if user:
            if user.is_active:
                return HttpResponseRedirect('/PantryPal_app/')
            else:
                # An inactive accountlogin(request, user) was used
                return HttpResponse("Your PantryPal_app account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # HTTP GET request
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'PantryPal_app/login.html', {})

def logout_view(request):
    logout(request)
    return render(request, "PantryPal_app/index.html", {})
