# ManyChat - DialogFlow Connector
Python-Flask project to connect ManyChat with Dialogflow.
This project uses Dialogflow Web Demo integration to handle a simple 
authentication and avoid complicated setup with Google Cloud credentials.


### Installation steps
1. In your ManyChat account, go to My Profile - Applications and Create New Application.
2. Enter the Name and Description of your App.
3. Copy the content from [manychat_json_app.json](manychat_json_app.json) 
and paste it in the JSON field.
4. Save your App and go back to Applications list.
5. Click in the right menu of your App and hit Install.
6. Select the page you want to install your App and install it.
7. Go to App Settings after successfully install your App.
8. Enter the server URL of where you have this Python project deployed.
9. Find the text right before the SAVE button and click in "Copy my app key".
10. Paste your ManyChat API Key in the corresponding field.
11. Go to your Dialogflow Agent - Settings and copy the Project ID,
then paste it in your ManyChat App Settings.
12. Go back to Dialogflow - Integrations and enable the Web Demo integration.
13. Click in the pencil icon and copy the Agent ID,
it should be something like this: _35g03j8r-cb33-21fa-89yh-90705s43f581_
14. Go to ManyChat App settings and paste the Dialogflow Agent ID.
15. Save your App settings.

Now all you need to do is add your Dialogflow Connector App to your 
Default Reply or any other flow inside ManyChat.




## About this project

This project is created and maintained by:
<br>
Github: daiangan<br/>
E-mail: daian@ganmedia.com<br/>
Website: https://ganmedia.com<br/>
