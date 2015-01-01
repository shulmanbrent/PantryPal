import json
import urllib, urllib2

def run_get(recipe_id):
	# Specified the root
    root_url = 'http://api.yummly.com/v1/api/recipe'

    # Setup authentication with the Yummly servers.
    yummly_app_id = '92d67e12'
    yummly_api_key = '1c9dd40cdaa1ee28b9a65429530fcfe6'

    get_url = "{0}/{1}?_app_id={2}&_app_key={3}".format(
    	root_url,
    	recipe_id,
    	yummly_app_id,
    	yummly_api_key)


    results = {}
    try:
        #Connect to the server and read the response generated.
        response = urllib2.urlopen(get_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)
        results['name'] = json_response['name']
        results['imageUrl'] = json_response['images'][0]['imageUrlsBySize']['360']
        results['ingredients'] = json_response['ingredientLines']
        results['sourceUrl'] = json_response['source']['sourceRecipeUrl']

        # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Yummly API: ", e

    return results