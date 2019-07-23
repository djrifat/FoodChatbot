# @Author: Daniël Jrifat
# Promts user to select between Vegetarian or a mix of all kinds of food
# Returns the correct respond according to the chosen food type(vegan of all) 

# Imports
import random
from foodResponses import (
    LIST_NO_ANSWER,
    LIST_VEG,
    LIST_MIX,
    LIST_SEARCH,
    LIST_EASY,
    LIST_MEDIUM,
    LIST_HARD,
    LIST_FOOD_NOT_OKAY
)

# Default message to return
speech = random.choice(LIST_NO_ANSWER)

# Selects recipe difficulty and returns matching reply to DialogFlow chatbot
# @PARAM: data parameter, get recipeComplexity from Dialogflow
# @RETURN: returns string, contains proper response
def selectDifficultyDish(data):
    
    # Get recipe complexity entity from Dialogflow
    # Complexity = data.get('queryResult').get('parameters').get('GerechtComplexiteit')
    complexity = data['queryResult']['parameters']['GerechtComplexiteit']

    # Check requested recipe complexity by the user
    if complexity == "Super easy":
        speech = random.choice(LIST_EASY)
    elif complexity == "Not too tricky":
        speech = random.choice(LIST_MEDIUM)
    elif complexity == "Showing off":
        speech = random.choice(LIST_HARD)
    else:
        speech = speech

    # Return proper response
    return {
        "fulfillmentText": "Text response",
        "fulfillmentMessages": [{
            "text": {
                "text": [speech]
                }
            }
        ],
        "source": "Flavourspace"
    }

# Selects foodtype and returns matching reply to DialogFlow chatbot
# @PARAM: data parameter, get foodtypes from Dialogflow
# @RETURN: returns string, contains proper response
def selectFoodType(data):
    # Get foodtype entity from Dialogflow
    food = data['queryResult']['parameters']['foodTypes']
        
    # Check what foodtype entity is being called
    if food == "Zoek op ingrediënten":
        speech = random.choice(LIST_SEARCH)  
    elif food == "Vegatarisch":
        speech = random.choice(LIST_VEG)
    elif food == "Mix van alles":
        speech = random.choice(LIST_MIX)
    
    else:
        speech = speech
    
    # Return proper response
    return {
        "fulfillmentText": "Text response",
        "fulfillmentMessages": [{
            "text": {
                "text": [speech]
                }
            }
        ],
        "source": "Flavourspace"
    }


# Selects foodtype and returns matching reply to DialogFlow chatbot
# @PARAM: data parameter, get foodtypes from Dialogflow
# @RETURN: returns string, contains proper response
def recipeNotGood(data):
    # Check if action matches   
    if data.get('queryResult').get('action') == "recipeNotOkay":
        speech = random.choice(LIST_FOOD_NOT_OKAY)
    else:
        speech = speech
    
    # Return proper response
    return {
        "fulfillmentText": "Text response",
        "fulfillmentMessages": [{
            "text": {
                "text": [speech]
                }
            }
        ],
        "source": "Flavourspace"
    }



