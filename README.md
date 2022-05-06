# ManyChat - DialogFlow Connector
Python-Flask project to connect ManyChat with Dialogflow.
This project uses Dialogflow Web Demo integration to handle a simple 
authentication and avoid complicated setup with Google Cloud credentials.

If you will not handle too much traffic, you can host this project for free in [https://repl.it/](Repl.it)
<br>
Just fork the project inside Repl.it, hit RUN and copy your server URL.

[![Run on Repl.it](https://repl.it/badge/github/daiangan/manychat-dialogflow-connector)](https://repl.it/github/daiangan/manychat-dialogflow-connector)


### Installation steps
1. In your ManyChat account, go to My Profile - Applications and Create New Application.
2. Enter the Name and Description of your App.
3. Copy the content from [manychat_json_app.json](manychat_json_app.json) 
and paste it in the JSON field.
4. Go to the API Access tab and select the following permissions:
    * View contact data
    * Manage contact data
    * Send messages
5. Save your App and go back to Applications list.
6. Click in the right menu of your App and hit Install.
7. Select the page you want to install your App and install it.
8. Go to App Settings after successfully install your App.
9. Enter the server URL of where you have this Python project deployed.
10. Find the text right before the SAVE button and click in "Copy my app key".
11. Paste your ManyChat API Key in the corresponding field.
12. Go to your Dialogflow Agent - Settings and copy the Project ID,
then paste it in your ManyChat App Settings.
13. Go back to Dialogflow - Integrations and enable the Web Demo integration.
14. Click in the pencil icon and copy the Agent ID,
it should be something like this: _35g03j8r-cb33-21fa-89yh-90705s43f581_
15. Go to ManyChat App settings and paste the Dialogflow Agent ID.
16. Save your App settings.

Now all you need to do is add your Dialogflow Connector App to your 
Default Reply or any other flow inside ManyChat.  

Thanks to Joren Wouters now we have a video explaining how to deploy and use this repo:  
https://www.youtube.com/watch?v=7HSfIxgcii8

### Dialogflow system entities  
If you use __sys.date-period__ you can add __startDate__ and __endDate__ to your ManyChat user fields.  




## About this project

This project is created and maintained by:
<br>
__Daian Gan__<br>
Github: [daiangan](https://github.com/daiangan)<br/>
E-mail: daian@ganmedia.com<br/>
Website: https://daiangan.com<br/>
