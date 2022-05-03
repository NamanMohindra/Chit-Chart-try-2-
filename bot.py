from flask import render_template
from twitchio.ext import commands
import nest_asyncio
import seaborn as sns
import matplotlib.pyplot as plt
import time
import requests as req
import regex
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from processing import Token_List,Chat_processor,Token,Tester
from shutil import copyfile
from collections import deque, defaultdict
import os 
nest_asyncio.apply()
sns.set_theme()

# array_of_64 = deque()
class Bot(commands.Bot):
    array_of_64 = deque()
    user_message_mapping = defaultdict(list)
    # def get_data_from_model():
    #     # print('------------Request found-------------------------')
    #     # print(len(Bot.array_of_64))
    #     if len(Bot.array_of_64) > 0:
    #         output = req.get('https://695f-104-196-119-181.ngrok.io/abcd', params={'string1': Bot.array_of_64})
    #     else:
    #         return '0'
    #     print(output)
    #     return output
    def __init__(self, refresh_flag = 0):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        self.nlp_processor = Chat_processor()
        self.mode = 1
        self.last_time_graph = time.time()
        self.last_time_graph_test = time.time()
        super().__init__(token='chd088egdk7ocqx4rbqs9ux367gckw', prefix='?', initial_channels=['xQcOW','NRG_Hamlinz','39daph','QuackityToo','TimTheTatman','ESL_CSGO','RanbooLive','xQcOW','Castro_1021','s1mple','Mongraal'])
        self.refresh_flag = refresh_flag


    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        if self.refresh_flag.value == 1:
            self.refresh()
            with self.refresh_flag.get_lock():
                if self.refresh_flag.value == 1:
                    self.refresh_flag.value -= 1

        # we need to process the message first before dictionary
        # remember to add rstrip and lstrip
        # print("in event_message")
        self.nlp_processor.process_string(message.content,message.author.name)

        # print('---------------------------------------------------------------------------------')
        # print('---------------------------MESSAGE AUTHOR AND CONTENT----------------------------')
        # print('MESSAGE IS ------', message.content)
        # print('AUTHOR IS -------', message.author.name)
        # need to run build graph once the program starts and then it will call itself after every n seconds
        # print('time difference')
        # print(time.time() - self.last_time_graph)
        # -`!^ (key) -`!~ (value) -`!~ (value) -`!~ (value)
        if len(Bot.array_of_64) <= 63:
            Bot.array_of_64.append(message.content)
        else:
            Bot.user_message_mapping[message.author.name].append(message.content)
            Bot.array_of_64.popleft()
            Bot.array_of_64.append(message.content)
        if len(Bot.user_message_mapping) <= 50:
            Bot.user_message_mapping[message.author.name].append(message.content)
        else:
            temp = ''
            for key, value in Bot.user_message_mapping.items():
                print('-`!^' + str(key))
                print('-`!~'.join(value))
                temp += '-`!^' + str(key) + '-`!~' + '-`!~'.join(value)
                print('----------------Key Change-------------------')
                print('-`!^' + str(key) + '-`!~' + '-`!~'.join(value))
            output = req.post('https://0396-35-230-8-187.ngrok.io/abcd', params = {'string1': temp})
            print(output)
            Bot.user_message_mapping = defaultdict(list)
        if time.time() - self.last_time_graph_test > 5:
            self.last_time_graph_test = time.time()
            temp = '-`!~'.join(list(Bot.array_of_64))
            output = req.post('https://0396-35-230-8-187.ngrok.io/abcd', params = {'string1': temp})
            print(output)
            self.build_toxicity_bar_graph(output)
        if time.time() - self.last_time_graph > 1:
            # print('---------------------------------------------------------------------------------')
            # print('---------------------------------GRAPH FUNCTIONS---------------------------------')
            # print(self.nlp_processor.getCommon())
            # print(self.nlp_processor.get_CPM())
            # print('---------------------------------------------------------------------------------')
            bar_graph_data = self.nlp_processor.getCommon()
            line_graph_data = self.nlp_processor.get_CPM()
            self.build_graph(bar_graph_data)
            self.build_line_graph(line_graph_data)
            self.last_time_graph = time.time()
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    def build_toxicity_bar_graph(self, inputs):
        x_axis = []
        y_axis = []
        for key, value in inputs.items():
            x_axis.append(key)
            y_axis.append(value)
        plt.figure(figsize=(10,8), dpi=500)
        plt.title("Sentiment levels",fontsize=30)
        ax = sns.barplot(x = x_axis, y = y_axis,palette=("plasma"))
        ax.set_xlabel('Sentiment Type', fontsize=16)
        ax.set_ylabel('Sentiment level', fontsize=16)
        plt.rcParams['font.size'] = '18'
        plt.savefig(r'./static/animal3.jpg')
    
    def build_graph(self,inputs):
        # we first sort the array and clean it to get it into plotting format
    
        # print('graph input')
        # print(inputs)
        x_axis = []
        y_axis = []
        for i in inputs:
            x_axis.append(i[0])
            y_axis.append(i[1])
        plt.figure(figsize=(10,8), dpi=500)
        plt.title("Word Frequency",fontsize=30)
        ax = sns.barplot(x = x_axis, y = y_axis,palette=("plasma"))
        ax.set_xlabel('Words', fontsize=16)
        ax.set_ylabel('Frequency', fontsize=16)
        plt.rcParams['font.size'] = '18'
        plt.savefig(r'./static/animal.jpg')


    def build_line_graph(self,inputs):
        # we first sort the array and clean it to get it into plotting format
        if inputs:
            # print('graph input')
            # print(inputs)
            x_axis = ['110','100','90','80','70','60','50','40','30','20','10','live']
            y_axis = inputs
            x = [1,2,3,4,5,6,7,8,9,10,11,12]
            plt.xticks(x, x_axis)
            plt.rcParams['font.size'] = '11'
            plt.figure(figsize=(10, 8), dpi=500)
            plt.title("Messages per minute",fontsize = 30)
            ax = sns.lineplot(x = x_axis, y = y_axis,marker='o',color='purple')
            ax.set_xlabel('Seconds before', fontsize=13)
            ax.set_ylabel('Frequency of Messages', fontsize=13)
            plt.fill_between(x = x_axis,y1 = y_axis,color = 'purple',alpha=0.65)
            plt.savefig(r'./static/animal2.jpg')

    # async def listen(self):
    #     while True:
    #         if self.refresh_flag:
    #             self.refresh()
    #             with self.refresh_flag.get_lock():
    #                 if self.refresh_flag.value == 1:
    #                     self.refresh_flag.value -= 1
    #         time.sleep(1000)
    
    def refresh(self):
        self.nlp_processor.command(0)
        # print("step 1")
        #os.remove(r'./static/animal.jpg')
        # print("step 2")
        copyfile(r'./animal.jpg','./static/animal.jpg')
        # print("step 3")

    
        

# def __init__():
#     bot = Bot()
#     bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
