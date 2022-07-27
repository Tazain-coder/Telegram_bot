import telebot
import requests
import random
import csv
import os
import sys
sys.path.insert(1, "Chat_Bot")
import main
sys.path.insert(2, "Get_Song")
import Get_song_driver
from dotenv import load_dotenv


API_KEY = "Your Api Key Here"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! nice to meet you")


@bot.message_handler(commands=["greet"])
def greet(message):
    bot.reply_to(message, "Hey!!")

@bot.message_handler(commands=["user"])
def user(message):
    bot.reply_to(message, (f"""User_id: {str(message.chat.id)},\nUsername: {str(message.chat.first_name)}"""))

@bot.message_handler(commands=["randomAnime"])

# Finction to call animeList
def get_anime(message):
    url = "https://jikan1.p.rapidapi.com/top/anime/1/upcoming"

    headers = {
        "X-RapidAPI-Key": "20fb1d1550mshd9e40f581614f3bp1eb721jsn7aa12ad98052",
        "X-RapidAPI-Host": "jikan1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    # bot.send_message(message.chat.id, "Looking for anime...")
    print()
    computer_choice = random.randint(1, 9000)
    computer_url = 'https://api.jikan.moe/v3/anime/{}/'.format(computer_choice)
    computer_response = requests.get(computer_url)
    # print(computer_response.json())
    bot.send_message(message.chat.id,f"computer's choice: {computer_response.json()['title']}")
    
#get entered text
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    bot.send_message(message.chat.id, main.chat(message.text))
    if main.tags(message.text) == 'song':
        sent = bot.send_message(message.chat.id, 'What Song You wanna hear? ')
        bot.register_next_step_handler(sent, hello)
        


@bot.message_handler(commands=['Song'])
def start(message):
  sent = bot.send_message(message.chat.id, ' ')
  bot.register_next_step_handler(sent, hello)

def Get_Song(message):
    text = Get_song_driver.Song(message.text)
    bot.send_message(message.chat.id, text)
    


bot.polling()