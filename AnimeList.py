import requests
import random


url = "https://jikan1.p.rapidapi.com/top/anime/1/upcoming"

headers = {
	"X-RapidAPI-Key": "20fb1d1550mshd9e40f581614f3bp1eb721jsn7aa12ad98052",
	"X-RapidAPI-Host": "jikan1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print("Now generating computer's choice...")
computer_choice = random.randint(1, 9000)
computer_url = 'https://api.jikan.moe/v3/anime/{}/'.format(computer_choice)
computer_response = requests.get(computer_url)
# print(computer_response.json())
print("computer's choice: ", computer_response.json()['title'])




@bot.message_handler(commands=['Song'])
def start(message):
  sent = bot.send_message(message.chat.id, 'What Song You wanna hear? ')
  bot.register_next_step_handler(sent, hello)

def hello(message):
    text = Get_song_driver.Song(message.text)
    bot.send_message(message.chat.id, text)