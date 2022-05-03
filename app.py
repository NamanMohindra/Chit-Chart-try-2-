from flask import Flask,render_template,request,redirect,url_for
import bot
from multiprocessing import Process, Manager, Value
import requests as req

import asyncio
app = Flask(__name__)
r_flag = None
bot_flag = 0

@app.route('/', methods=['GET','POST'])
def home():
    print('hi')
    global r_flag
    global bot_flag
    if bot_flag == 0:
        global r_flag
        refresh_flag = Value('i', 0)
        r_flag = refresh_flag
        p1 = Process(target=func2, args=[refresh_flag])
        p1.start()
        bot_flag = 1
    if request.method == "POST":
        value = request.form.to_dict()
        if 'Refresh' in value:
            with r_flag.get_lock():
                if r_flag.value == 0:
                    r_flag.value += 1
            # do something
            return render_template("index.html")
        elif 'Polls' in value:
            # do something else
            pass
        else:
            # do nothing
            pass
        
    else:
        return render_template("index.html")

# @app.route("/something")
# def enter():
#     # global bot_flag
#     # if bot_flag == 0:
#     #     global r_flag
#     #     refresh_flag = Value('i', 0)
#     #     print("refresh_flag type:", type(refresh_flag))
#     #     r_flag = refresh_flag
#     #     print("main start")
#     #     p1 = Process(target=func2, args=[refresh_flag])
#     #     p1.start()
#     #     bot_flag = 1
#     return redirect(url_for("home"))
#     # p1.join()
#     # print("main end")
#     # return redirect(url_for("home"))

# @app.route('/generateGraphs', methods=['GET'])
# def getGraphsData():
#     print('------------Request set-------------------------')
#     return bot.Bot.get_data_from_model()


def func2(refresh_flag):
    ourBot = bot.Bot(refresh_flag)
    ourBot.run()

# def main():
#     global r_flag
#     refresh_flag = Value('i', 0)
#     print("refresh_flag type:", type(refresh_flag))
#     r_flag = refresh_flag
#     print("main start")
#     p1 = Process(target=func2, args=[refresh_flag])
#     p1.start()
#     print("before app.run")
#     app.run(debug=True)
#     p1.join()
#     print("main end")

if __name__ == '__main__':
    #main()
    app.run(debug=True)