import json
import urllib, urllib2
from PantryPal_app.run_get import run_get

def run_query(search_terms, max_time, offset):
    # Specified the root
    root_url = 'http://api.yummly.com/v1/api/recipes?'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With maxResults = 10 and start = 11, this would start from page 2.
    maxResult = 1000
    start = 0

    # Setup authentication with the Yummly servers.
    yummly_app_id = '92d67e12'
    yummly_api_key = '1c9dd40cdaa1ee28b9a65429530fcfe6'

    search_terms = search_terms.split()
    
    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}_app_id={1}&_app_key={2}&requirePictures=true&maxResult={3}&start={4}&maxTotalTimeInSeconds={5}".format(
        root_url,
        yummly_app_id,
        yummly_api_key,
        maxResult,
        start,
        max_time)
    
    # for term in query:
    #     ingredient = "&allowedIngredient[]={0}".format(
    #         term)
    #     search_url += ingredient


    if search_terms:
        for term in search_terms:
            if "_" in term:
                term = term.replace("_", "%20")
            ingredient = "&allowedIngredient[]={0}".format(
                term)
            search_url += ingredient    


    # Create a 'password manager' which handles authentication for us.
    #password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    #password_mgr.add_password(None, search_url, username, bing_api_key)

    # Create our results list which we'll populate.
    results = []

    try:
         #Connect to the server and read the response generated.
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Check is results empty to prevent running through the rest of the code
        # if not json_response['matches']: return results

        # Sort results based on number of ingredients
        r = json_response['matches']

        if r:
            r = sorted(r, cmp=lambda x,y: cmp(len(x['ingredients']), len(y['ingredients'])))

            counter = 0
            start_index = (offset - 1) * 16 
            for recipe in r[start_index:]:
                counter += 1
                if counter > 16: break
                r_id = recipe['id']
                results.append(run_get(r_id, len(search_terms)))

        # Loop through each page returned, populating out results list.
        #for result in json_response['d']['results']:
        #    results.append({
        #        'title': result['Title'],
        #        'link': result['Url'],
        #        'summary': result['Description']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Yummly API: ", e

    # Return the list of results to the calling function.
    return results