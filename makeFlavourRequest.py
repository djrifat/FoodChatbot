# @Author: Daniël Jrifat
# DIALOGFLOW: RandomFoobar
# HEROKU: Flavour

# Imports
import requests
from random import randint

# Base URL for FLavourspace API requests
__baseUrl = "http://52.59.154.51/api/recipes/"
      
# @BRIEF: Retrieves data from Flavourspace API
# @PARAM: req, request the specified action on DIalogflow) parameter
# @PARAM: vegan(bool), specifies if the recipes should be vegan or mixed
# @PARAM: cookingTime(string), specifies the amount of cookingtime
# @PARAM: recipeComplexity(string), specifies the complexity of the recipe
# @RETURN: returns flavourspace data
def flavourData(req, vegan):
    # Get neccesary parameters from Dialogflow
    productToUse = getProduct(req)
    timeToCook = getCookingTime(req)
    complexity = getRecipeComplexity(req)
    # API headers
    headers = {
            'Authorization': "Token 38189c8e0321694be206fbdc8f7158066648fb5e",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
    # Query string containing parameters to pass to API
    queryString = { 
        "search": productToUse, 
        "vegetarian": vegan,
        "difficulty":complexity, 
        "cooking_time__icontains":timeToCook
    }
    # Make request
    flavoRequest = requests.get(url=__baseUrl, headers=headers, params=queryString)
    # Parse request to readable JSON format
    flavoData = flavoRequest.json()
    return flavoData

# Fetches data from Flavourspace API
# @PARAM: req(request the specified action on DIalogflow) parameter
# @PARAM: vegan(bool), specifies if the recipes should be vegan or mixed
# @RETURN: returns flavourspace data
def randomFlavourData():
    # API headers
    headers = {
            'Authorization': "Token 38189c8e0321694be206fbdc8f7158066648fb5e",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
    # List to store JSON results
    storedFlavour = []
    for i in range(0,3):
            # Base url to approach API
            baseUrl = "http://52.59.154.51/api/recipes/" + str(randint(3, 1000))
            # Make request
            flavoRequest = requests.get(url=baseUrl, headers=headers)
            # Parse request to readable JSON format
            flavoData = flavoRequest.json()
            storedFlavour.append(flavoData)
    return storedFlavour



# Retrieves data from Flavourspace API
# @PARAM: req, request the specified action on DIalogflow) parameter
# @PARAM: vegan(bool), specifies if the recipes should be vegan or mixed
# @PARAM: cookingTime(string), specifies the amount of cookingtime
# @PARAM: recipeComplexity(string), specifies the complexity of the recipe
# @RETURN: returns flavourspace data
def flavourDataRecipeNotOke(req, vegan):
    # Get neccesary parameters from Dialogflow
    productToUse = getContextProduct(req)
    timeToCook = getCookingTime(req)
    complexity = getRecipeComplexity(req)
    # API headers
    headers = {
            'Authorization': "Token 38189c8e0321694be206fbdc8f7158066648fb5e",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
    # Query string containing parameters to pass to API
    queryString = { 
        "search": productToUse, 
        "vegetarian": vegan,
        "difficulty":complexity, 
        "cooking_time__icontains":timeToCook
    }
    # Make request
    flavoRequest = requests.get(url=__baseUrl, headers=headers, params=queryString)
    # Parse request to readable JSON format
    flavoData = flavoRequest.json()
    return flavoData


# Get "products" parameter from Dialogflow, returns parameter with associated value
# @RETURN: returns entity requested by user
def getContextProduct(req):
    # Acces desired level in JSON data

    # TODO:
    # FIX OUTPUTCONTEXT
    result = req.get('queryResult')
    outputContext = result.get('outputContexts')
    parameters = outputContext.get('parameters') 
    productContext = parameters.get('products')
    # TODO make response for empty product
    if productContext is None:
        return " "
    return productContext
    
# Get "products" parameter from Dialogflow, returns parameter with associated value
# @RETURN: returns entity requested by user
def getProduct(req):
    # Acces desired level in JSON data
    result = req.get('queryResult')
    parameters = result.get('parameters')
    product = parameters.get('products') 
    # TODO make response for empty product
    if product is None:
        return " "
    return product
    
# Get "CookingTime" parameter from Dialogflow, returns parameter with associated value
# @RETURN: returns entity requested by user
def getCookingTime(req):
    # Acces desired level in JSON data
    result = req.get('queryResult')
    parameters = result.get('parameters')
    cookingTime = parameters.get('CookingTime')
    # TODO make response for empty product
    if cookingTime is None:
        return " "
    return cookingTime
    
# Get "GerechtComplexiteit" parameter from Dialogflow, returns parameter with associated value
# @RETURN: returns entity requested by user
def getRecipeComplexity(req):
    # Acces desired level in JSON data
    result = req.get('queryResult')
    parameters = result.get('parameters')
    gerechtComplexiteit = parameters.get('GerechtComplexiteit')
    # TODO make response for empty product
    if gerechtComplexiteit is None:
        return " "
    return gerechtComplexiteit