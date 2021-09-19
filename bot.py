from twitchio.ext import commands
import nest_asyncio
import seaborn as sns
import matplotlib.pyplot as plt
import time
import regex
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import deque
from processing import Token_List,Chat_processor,Token,Tester
from shutil import copyfile
import os 
nest_asyncio.apply()

class Bot(commands.Bot):

    def __init__(self, refresh_flag):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        print("Bot created")
        self.nlp_processor = Chat_processor()
        self.mode = 1
        self.last_time_graph = time.time()
        super().__init__(token='chd088egdk7ocqx4rbqs9ux367gckw', prefix='?', initial_channels=['bananashooter07'])
        self.refresh_flag = refresh_flag

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

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
        self.nlp_processor.process_string(message.content,message.author.name)
        
        
        # need to run build graph once the program starts and then it will call itself after every n seconds
        print('time difference')
        print(time.time() - self.last_time_graph)
        
        if time.time() - self.last_time_graph > 1:
            self.build_graph(self.nlp_processor.getCommon())
            self.build_line_graph(self.nlp_processor.get_CPM())
            self.last_time_graph = time.time()
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)
    
    def build_graph(self,inputs):
        # we first sort the array and clean it to get it into plotting format
    
        print('graph input')
        print(inputs)
        x_axis = []
        y_axis = []
        for i in inputs:
            x_axis.append(i[0])
            y_axis.append(i[1])
        plt.figure(figsize=(10,8))
        plt.title("Word Frequency",fontsize=30)
        ax = sns.barplot(x = x_axis, y = y_axis,palette=("Purples_r"))
        ax.set_xlabel('Words', fontsize=16)
        ax.set_ylabel('Frequency', fontsize=16)
        plt.rcParams['font.size'] = '18'
        plt.savefig(r'./static/animal.jpg')
        print('graph was printed')


    def build_line_graph(self,inputs):
        # we first sort the array and clean it to get it into plotting format
        if inputs:
            print('graph input')
            print(inputs)
            x_axis = ['110','100','90','80','70','60','50','40','30','20','10','live']
            y_axis = inputs
            plt.rcParams['font.size'] = '14'
            plt.figure(figsize=(10,8))
            plt.title("Messages per minute",fontsize = 30)
            ax = sns.lineplot(x = x_axis, y = y_axis,marker='o',color='purple')
            ax.set_xlabel('Seconds before', fontsize=16)
            ax.set_ylabel('Messages per minute', fontsize=16)
            plt.savefig(r'./static/animal2.jpg')
            print('lineplot was printed')

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
        print("step 1")
        #os.remove(r'./static/animal.jpg')
        print("step 2")
        copyfile(r'./animal.jpg','./static/animal.jpg')
        print("step 3")

    
        

# def __init__():
#     bot = Bot()
#     bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
