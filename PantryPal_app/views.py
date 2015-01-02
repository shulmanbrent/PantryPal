import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from PantryPal_app.run_query import run_query


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Yummly function to get the results list!
            result_list = run_query(query)


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
        # converstion to seconds

        if request.POST['time']:
            max_time = str(int(request.POST['time']) * 60)
        else:
            max_time = '3600'

        # Run our Yummly function to get the results list!
        result_list = run_query(search_terms, max_time)


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('PantryPal_app/search.html', {'result_list': result_list}, context)

# def recipes(request):
#     context = RequestContext(request)

#     return render_to_response('PantryPal_app/recipes.html', context)