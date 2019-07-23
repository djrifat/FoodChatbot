# @Author: Daniël Jrifat
# DIALOGFLOW: RandomFoobar
# HEROKU: Flavour
 
# Imports
from __future__ import print_function

import json, os, sys

from flask import Flask, make_response, request
from future.standard_library import install_aliases
from random import randint
import dialogflow_v2 as dialogflow

import wehbookResults as webResult
import makeFlavourRequest as flavourReq
import chooseFoodType as chooseFood

install_aliases()


# Flask app should start in global layout
app = Flask(__name__)

# Verify token for Dialogflow and Facebook connection
verify_token = "foo"

# Routes
@app.route('/', methods=['GET'])
# Webhook verification for FB
def verify():
    # Endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == verify_token:
            return "Verification token mismatch", 403
        raise ValueError('FB_VERIFY_TOKEN does not match.')
        return request.args["hub.challenge"], 200
    return 'Hello World (from Flask!)', 200


@app.route('/webhook', methods=['POST'])
# Webhook handles the http requests for the Dialogflow webhook
def webhook():
    req = request.get_json(silent=True, force=True)
    print("REQ:", req)
    res = processRequest(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print(r)
    return r
 

# Process JSON request 
def processRequest(req):
    # **Text between () in comments is the corresponding intent in Dialogflow**
    # Request action from Dialogflow
    
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    # WELCOME MESSAGE
    if action == "fbWelcome":
        res = webResult.FBWelcomeWebhookResult()
        print(action)

    # (SearchRecipe)Set the food type, VEGA 
    elif action == "SearchRecipe-Vega":
        res = chooseFood.selectFoodType(req)
        print(action)
    # (HelpMeFindReci
    # (SearchRecipe)Set the food type, MIXED
    elif action == "SearchRecipe-Mix":
        res = chooseFood.selectFoodType(req)
        print(action)
    # (HelpMeFindRecipe) SEARCH INGREDIENT
    elif action == "Helpme-SearchIngredient":
        res = chooseFood.selectFoodType(req)
        print(action)

    
    # WEBHOOK RESULTS
    # Create webhook result VEGA
    elif action == "SearchRecipe-Vega-Response":
        data = flavourReq.flavourData(req, True)
        res = webResult.webhookResult(data)
    # Create webhook result MIXED
    elif action == "SearchRecipe-Mix-Response":
        data = flavourReq.flavourData(req, False)
        res = webResult.webhookResult(data)

    # Create webhook result SEARCH INGREDIENT
    elif action == "HelpFindRecipe-Response":
        data = flavourReq.flavourData(req, False)
        res = webResult.webhookResult(data)
    # Create webhook result QUESTIONAIRE
    elif action == "HelpMeFindRecipe-Question-Response":
        data = flavourReq.flavourData(req, False)
        res = webResult.webhookResultQuestionaire(data, req)

    # Response if recipe is not OKE
    elif action == "recipeNotOkay":
        data = flavourReq.flavourData(req, False)
        res = webResult.webhookResultDontLikeRecipe(data)
        print(action)
    elif action == "recipeNotOkayVega":
        data = flavourReq.flavourDataRecipeNotOke(req, True)
        res = webResult.webhookResultDontLikeRecipe(data)
        print(action)

    # Create webhook result SUPRISEME
    elif action == "SupriseMe":
        data = flavourReq.randomFlavourData()
        res = webResult.supriseWebhookResult(data)
    # Create webhook result USER ONLY SAYS RECIPE
    elif action == "UserSaysOnlyRecipe":
        data = flavourReq.flavourData(req, False)
        res = webResult.webhookResult(data)
    else:
        res = webResult.fallback()
    return res

# Print requests in terminal
def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
