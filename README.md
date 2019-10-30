# Flavourspace Virtual Souschef

[![N|Solid](https://pbs.twimg.com/profile_images/469110013898661888/u9CeOkTw_200x200.png)](http://flavourspace.com/)

###### Flavourspace Virtual Sous chef is a chatbot currently deployed on Facebook (still in development)
> This document contains an installation and setup guide
> for the Flavourspace chatbot. Follow the steps to make sure 
> the chatbot is properply set up. After all nessecary accounts are created
> make sure all software is properly installed. Make sure this is done
> correctly. This allows the chatbot to work as it should.

### Tech requirements
Flavourspace chatbot uses a number of open source projects and services to work properly, the following technologies and services are mandatory for the chatbot to work.

* [Python](https://www.python.org/) - An interpreted, high-level, general-purpose programming language
* [JSON](https://docs.python.org/3/library/json.html) - JavaScript Object Notation is a lightweight data-interchange forma
* [Dialogflow](https://dialogflow.com/) - Natural Language Processing engine from Google


### Account requirements
To use the Flavourspace chatbot a number of accounts need to be created, in order for the chatbot to work properly.
* [Dialogflow account](https://dialogflow.com/) - Natural Language Processing engine from Google
* [Facebook Developer account](https://www.facebook.com/) - Online Social media platform
* [Heroku account](https://www.heroku.com/) - Cloud platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud


### Installation
Flavourspace chatbot requires [Python](https://www.python.org/) v3.0+ to run.
Python is not installed on windows devices by default. Make sure Python version 3 or higher is installed. If u do not know how to do this, follow this guide [Python install guide](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)

Check if python is properly installed.
```sh
python --version
RESULT: Python 3.7.0
```


Pip is the package manager which is used by Python. This package manager allows u to download and install Python packages through the command line. Follow this [guide](https://www.liquidweb.com/kb/install-pip-windows/) to install PIP.
(If u have downloaded the newest Python version, u DON'T need to seperatly install PIP.)

Check if Pip is properly installed.
```sh
pip -V
RESULT: pip 18.0 from c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
```

### Packages
Flavourspace chatbot is currently uses the following packages. Instructions on how to download and install them in your own environment are linked below. 

**Note:** 
Install [`Virtualenv`](https://virtualenv.pypa.io/en/latest/installation/) before installing any other packages. [`Virtualenv`](https://virtualenv.pypa.io/en/latest/installation/) is a tool used to create an isolated Python environment. This environment has its own installation directories that doesn't share libraries with other virtualenv environments (and optionally doesn't access the globally installed libraries either). 
Virtualenv is the easiest and recommended way to configure a custom Python environment.

| Package | Install |
| ------ | ------ |
| Request | ```python -m pip install request ``` |
| Flask | [flask.pocoo.org/docs/1.0/installation/][Plflsk] |
| Dialogflow_v2 | [dialogflow-python-client-v2/master/README.rst][Pldialog] |



### Checklist
Make sure the following requirements are met before continuing. When all requirements are met, follow the steps in the setup guide.
#### Accounts
- [ ] Dialogflow account
- [ ] Facebook Developer account
- [ ] OPTIONAL: Heroku account

#### Tech
- [ ] Python version 3.0+
- [ ] Pip
- [ ] Virtualenv
- [ ] Dialogflow_v2
- [ ] Flask
- [ ] Request

##### After all above steps are executed correctly, it is time to connect Dialogflow with Facebook.

### Setting up Facebook

In order to set up the Facebook integration for your agent, you'll need the following:
- a Facebook Developer account
- a Facebook page to connect to add your agent (chatbot) to
#### Create a facebook app
1. Log into the [Facebook Developer console](https://developers.facebook.com/)
2. Click on **My Apps** in the upper right hand corner
3. Click on **Add a new page** and enter a name and contact email address
4. Click ***Create App ID*

![](https://dialogflow.com/docs/images/integrations/facebook/001-facebook.png)

5. On the next page, click the ***Get Started** button for the **Messenger** option
6. Under the **Token Generation** section, choose one of your Facebook pages

![](https://dialogflow.com/docs/images/integrations/facebook/002-facebook.png)
This will generate a **Page Access Token.** Keep this token handy, as you'll need to enter it in Dialogflow.

### Setting up Dialogflow
1. Click on the Integrations option in the left menu and switch on Facebook Messenger. In the dialog that opens, enter the following information: 
    - **Verify Token** - This can be any string and is solely for your purposes
    - **Page Access Token** - Enter the token generated in the Facebook Developer Console
2. Click the **Start** button

![](https://dialogflow.com/docs/images/integrations/facebook/003-facebook.png)

---
> **Note:** Keep the Callback URL and Verify Token handy for configuring the webhook.
---
### Webhook Configuration
To configure your agent's webhook, return to the Facebook Developer Console:
1. Click the **Setup Webhooks** button under the **Webhooks** section and enter the following information: 
    - **Callback URL** - This is the URL provided on the Facebook Messenger integration page
    - **Verify Token** - This is the token you created
    - Check **All Options**.
2. Click the **Verify and Save button**

![](https://dialogflow.com/docs/images/integrations/facebook/004-facebook.png)

You'll be taken back to the settings page and **Webhooks** should have a "Complete" status.
---
> **Note:** If you're using rich messages, be sure the messaging_postbacks option is checked.
---

### Optional Testing
In order to make your agent available for testing, you'll need to make your app public:
1. Click on **App Review** in the left menu of the Facebook Developer Console.
2. Click on the switch under **Make APP_NAME public?** You'll be prompted to choose a category for your app.
3. Choose **Apps for Messenger** from the list
4. Click the **Confirm** button.

![](https://dialogflow.com/docs/images/integrations/facebook/005-facebook.png)
You will also need to set a username for your page. This is the username users will chat with when using your agent. To set the username, click the Create Page @Username link under your page's profile picture and title.

![](https://dialogflow.com/docs/images/integrations/facebook/add-username.png)

---
> **Note:** You can make your app available for testing by adding testers to the app. To do this click on **Roles** in the left menu and then add people in the **Testers** section.
---
#### Follow [**this link**](https://dialogflow.com/docs/integrations/facebook) to the Dialogflow setup page.




   [Plreq]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [Plflsk]: <http://flask.pocoo.org/docs/1.0/installation/>
   [Pldialog]: <https://github.com/googleapis/dialogflow-python-client-v2/blob/master/README.rst>

