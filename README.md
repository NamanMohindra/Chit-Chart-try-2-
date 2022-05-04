Introduction 

Hello, we are Chit Chart, composed of 4 members, Ishtdeep Singh, John Lee, Naman Mohindra, and Amy Tan. Chit Chart is an application which captures chat in live streams in twitch and provides Live analysis and feedback to the streamer which can help the streamer improve the quality of stream.

Requirements

Python 3.8 and above

INSTALLATION
For Mac users - 
To install all the required packages/modules
open a terminal in the same directory as the repository and then run the command

pip install -r requirements.txt

For Windows Users

To install the required packages/moduls
open a terminal in the same directory as the repository and then run the command 

pip install -r requirements_windows.txt

If you face any errors regarding any modules in windows you can try to install
pipwin and then install the packages in which the error occurred through pipwin.

HOW TO RUN

If running the jupyter notebook locally(not recommended), run the two cells containing the lines 
```
server.run_app(app = app)
```
in both the jupyter notebooks and copy the localhost url 
```
http://localhost:10000
```
into the sentiment_classifier_connection_string and toxicity_classifier_connection_string variables in the bot.py file. This spins up the 2 classifiers as jupyter notebook servers.

If using google colab to run the 2 models(recommended), copy the url that looks something like 
```
NgrokTunnel: "https://xxxx-xx-xx-xx-xx.ngrok.io"
```
into the two variables named sentiment_classifier_connection_string and toxicity_classifier_connection_string.

Note that the string from the file name 'ML_Project_sentiment_classifier' must be pasted into the variable sentiment_classifier_connection_string and the url from the file name 'ML_Project_toxicity_classifier' must be pasted into the variable toxicity_classifier_connection_string. This way you can set up the server on google colab(recommended).

To run the local flask application to view the streamer-UI, run the command

python "app.py" 

in the terminal when you are in the same directory as the repository to run the application.
In a few seconds there will be an ip address and port displayed on the terminal screen.
Copy paste this url(usually http://127.0.0.1:5000/) into any web browser and the app will start running.

