# @Author: Daniël Jrifat

import random
import chooseFoodType as chooseFood
from foodResponses import (
    LIST_FOOD_NOT_OKAY,
    LIST_FB_WELCOME,
    LIST_NO_ANSWER,
    LIST_LIKE_RECIPE,
    LIST_FIND_RECIPE,
    LIST_VEG,
    LIST_MIX,
    LIST_SEARCH,
    LIST_EASY,
    LIST_MEDIUM,
    LIST_HARD
)

      
# Webhook result "vegan/mixed" intent 
def webhookResult(data):
      
    # Random number generator
    # Select random selection from recipe list
    randRecipeNr = random.sample(range(0, 10), 3)
    __baseUrl = "http://52.59.154.51"
    
    return {
      "fulfillmentMessages": [
        {
          "card": {
            "title": data['results'][randRecipeNr[0]]['title'],
            "subtitle": data['results'][randRecipeNr[0]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[0]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[0]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[1]]['title'],
            "subtitle": data['results'][randRecipeNr[1]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[1]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[1]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[2]]['title'],
            "subtitle": data['results'][randRecipeNr[2]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[2]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[2]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "text": {
            "text": [
              random.choice(LIST_LIKE_RECIPE)
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
    }


# Webhook result "Questionaire" intent 
def webhookResultQuestionaire(data, req):
      
    # Get recipe complexity entity from Dialogflow
    # Complexity = data.get('queryResult').get('parameters').get('GerechtComplexiteit')
    complexity = req['queryResult']['parameters']['GerechtComplexiteit']

    # Check requested recipe complexity by the user
    if complexity == "Super easy":
        speech = random.choice(LIST_EASY)
    elif complexity == "Not too tricky":
        speech = random.choice(LIST_MEDIUM)
    elif complexity == "Showing off":
        speech = random.choice(LIST_HARD)
    else:
        speech = speech
      
    # Random number generator
    # Select random selection from recipe list
    randRecipeNr = random.sample(range(0, 10), 3)
    __baseUrl = "http://52.59.154.51"
    
    return {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              speech
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[0]]['title'],
            "subtitle": data['results'][randRecipeNr[0]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[0]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[0]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[1]]['title'],
            "subtitle": data['results'][randRecipeNr[1]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[1]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[1]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[2]]['title'],
            "subtitle": data['results'][randRecipeNr[2]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[2]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[2]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "text": {
            "text": [
              random.choice(LIST_LIKE_RECIPE)
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
    }


# Webhook result recipe "NOT OKE" intent
def webhookResultDontLikeRecipe(data):
      
    randRecipeNr = random.sample(range(0, 50), 3)
    __baseUrl = "http://52.59.154.51"

    return {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              random.choice(LIST_FOOD_NOT_OKAY)
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[0]]['title'],
            "subtitle": data['results'][randRecipeNr[0]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[0]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[0]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[1]]['title'],
            "subtitle": data['results'][randRecipeNr[1]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[1]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[1]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data['results'][randRecipeNr[2]]['title'],
            "subtitle": data['results'][randRecipeNr[2]]['cooking_time'],
            "imageUri": __baseUrl + data['results'][randRecipeNr[2]]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data['results'][randRecipeNr[2]]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "quickReplies": {
            "title": random.choice(LIST_LIKE_RECIPE),
            "quickReplies" : [
              "Meer recepten",
              "Super!"
            ]
          },
          "platform": "FACEBOOK"
        }       
      ]
  }


# Webhook response for "SupriseMe" intent
def supriseWebhookResult(data):
      
    __baseUrl = "http://52.59.154.51"

    return {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              random.choice(LIST_FIND_RECIPE)
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data[0]['title'],
            "subtitle": data[0]['cooking_time'],
            "imageUri": __baseUrl + data[0]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data[0]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data[1]['title'],
            "subtitle": data[1]['cooking_time'],
            "imageUri": __baseUrl + data[1]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data[1]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": data[2]['title'],
            "subtitle": data[2]['cooking_time'],
            "imageUri": __baseUrl + data[2]['image_url'],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": data[2]['source_url']
              }, 
              {
                "text": "Delen",
                "postback": "https://www.facebook.com/"
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "quickReplies": {
            "title": random.choice(LIST_LIKE_RECIPE),
            "quickReplies" : [
              "Meer recepten",
              "Super!"
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
  }
  

# Webhook result "WELCOME" INTENT
def FBWelcomeWebhookResult():
    __baseUrl = "http://52.59.154.51"

    return {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              "Hii daar!\nIk ben de Flavourspace chatbot 👨‍🍳👋",
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": "Ik kom je helpen met het koken van wat lekkers! 🍕🥗",
            "subtitle": random.choice(LIST_FB_WELCOME),
            "imageUri": "https://images.pexels.com/photos/1070880/pexels-photo-1070880.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "buttons": [
              {
                "text": "Zoeken op recept",
                "postback": "Zoeken op recept" 
              },
              {
                "text": "Help mij zoeken",
                "postback": "Help mij zoeken" 
              },
              {
                "text": "Verras mij",
                "postback": "Verras mij" 
              },
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
  }


# Webhook result "FALLBACK" INTENT
def fallback():

    return {
      "fulfillmentMessages": [
        {
          "quickReplies": {
            "title": random.choice(LIST_NO_ANSWER),
            "quickReplies" : [
              "Zoeken op recept",
              "Help mij zoeken",
              "Verras mij"
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
  }








