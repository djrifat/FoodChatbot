import requests, json
import random 

def keys_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if type(element) is not dict:
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            keys = randint(3,1000)
            return keys
    return True


# Check if key exsist in dict
def keyCheck(key, arr, default):
    if key in arr.keys():
        return arr[key]
    else:
        return default

# Recursive method to test print returned JSON data
def test(n):
    bar = randint(1,50)
    daan = data['results'][bar]
    title = daan['title']
    foodId = daan['id']
    if n == 1:
        return 0
    else:
        res = n * test(n-1)       
        try:
            print("ID:" , foodId, "/", "TITLE:", title)
        except IndexError:
            bar = randint(1,10)
        return res


def lol():
      
    headers = { 
            'Authorization': "Token 38189c8e0321694be206fbdc8f7158066648fb5e",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
    testoe = []
    for i in range(0,3):
        # Base url to approach API
        baseUrl = "http://52.59.154.51/api/recipes/"         
        querystring = {"difficulty":"Not too tricky","cooking_time__icontains":"1h"}
        flavoRequest = requests.get(url=baseUrl, headers=headers, params=querystring)
        flavoData = flavoRequest.json()
        testoe.append(flavoData)

    return testoe[0]
    #return print(isinstance(flavoData, dict))

#lol()



import functools

def trackcalls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper

@trackcalls
def example():
    pass


#example()

#Actual Code!:
#if example.has_been_called:
    #print("foo bar")


# Webhook result "vegan/mixed" intent 
def webhookResult():
      
    # Random number generator
    # Select random selection from recipe list
    randRecipeNr = random.sample(range(0, 10), 3)
    __baseUrl = "http://52.59.154.51"
    
    return {
      "fulfillmentMessages": [
        {
          "card": {
            "title": [randRecipeNr[0]],
            "subtitle": [randRecipeNr[0]],
            "imageUri": [randRecipeNr[0]],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": [randRecipeNr[0]]
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": [randRecipeNr[1]],
            "subtitle": [randRecipeNr[1]],
            "imageUri": [randRecipeNr[1]],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": [randRecipeNr[1]]
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "card": {
            "title": [randRecipeNr[2]],
            "subtitle": [randRecipeNr[2]],
            "imageUri": [randRecipeNr[2]],
            "buttons": [
              {
                "text": "Bekijk recept",
                "postback": [randRecipeNr[2]]
              }
            ]
          },
          "platform": "FACEBOOK"
        },
        {
          "text": {
            "text": [
              "YOEYOE"
            ]
          },
          "platform": "FACEBOOK"
        }
      ]
    }

#webhookResult(lol())
#print(random.sample(range(0, 10), 3))
#print(lol())

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
            baseUrl = "http://52.59.154.51/api/recipes/" + str(random.randint(3, 1000))
            #queryString = {"vegetarian": vegan}
            # Make request
            flavoRequest = requests.get(url=baseUrl, headers=headers)
            # Parse request to readable JSON format
            flavoData = flavoRequest.json()
            storedFlavour.append(flavoData)
    return storedFlavour

#andomFlavourData()

def randomWebhookResult(data):
    # Set necessary variables to return to Dialogflow
    baseUrl = "http://52.59.154.51"               
    speech = ("I found this: " + data[0]['title'])

    # JSON response format to return to Facebook Messengerg
    randomResponse = {
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"generic",
            "elements":[
              {
                "title": data[0]['title'],
                "image_url": baseUrl + data[0]['image_url'],
                "subtitle": data[0]['cooking_time'],
                "default_action": {
                  "type": "web_url",
                  "url": data[0]['source_url'],
                  "webview_height_ratio": "full",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url": data[0]['source_url'],
                    "title":"Bekijk recept"
                  }, {
                    "type":"web_url",
                    "url": "https://www.facebook.com/",
                    "title":"Delen"
                  }              
                ]      
              },
              {
                "title": data[1]['title'],
                "image_url": baseUrl + data[1]['image_url'],
                "subtitle": data[1]['cooking_time'],
                "default_action": {
                  "type": "web_url",
                  "url": data[1]['source_url'],
                  "webview_height_ratio": "full",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url": data[1]['source_url'],
                    "title":"Bekijk recept"
                  }, {
                    "type":"web_url",
                    "url": "https://www.facebook.com/",
                    "title":"Delen"
                  }              
                ]      
              },
              {
                "title": data[2]['title'],
                "image_url": baseUrl + data[2]['image_url'],
                "subtitle": data[2]['cooking_time'],
                "default_action": {
                  "type": "web_url",
                  "url": data[2]['source_url'],
                  "webview_height_ratio": "full",
                },
                "buttons":[
                  {
                    "type":"web_url",
                    "url": data[2]['source_url'],
                    "title":"Bekijk recept"
                  }, {
                    "type":"web_url",
                    "url": "https://www.facebook.com/",
                    "title":"Delen"
                  }              
                ]      
              }
            ]
          }
        }
    }

    return {
        "data": {
            "facebook": randomResponse   
        }         
    }


#print(webhookResult())
#print(random.sample(range(0, 10), 3))

testje = {
    "setting_type": "call_to_actions",
    "thread_state": "existing_thread",
    "call_to_actions": [
        {"type": "web_url",
        "title": "test",
        "url": "https://test.com"
        },
      {
        "type": "postback",
        "title": "Help",
        "payload": "help"
      },
      {
        "type": "postback",
        "title": "Website",
        "payload": "web"
      }
    ]
  }
  
