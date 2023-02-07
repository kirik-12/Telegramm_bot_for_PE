import telebot
from telebot import types
import foto as ft
import random


API_TOKEN = '6072418722:AAFkuqO-wt9XlzF9_Z1btbAnIczV2Jx8Eyo'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}

question = ft.all_photos
random.shuffle(question)
n = 3 # количество вопросов
question = question[0:n] # теперь у нас целых 5 вопросов

class User:
    def __init__(self, *answers):
        self.answers = answers
        self.user_id = None
        self.try_today = None

    def append_answers(self, next_answer):
        all_answers = list(self.answers)
        all_answers.append(next_answer)
        self.answers = all_answers

        

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, """Hi there, I am Testing bot. Now I am telling for you rules""")
    bot.send_photo(message.chat.id, ft.map_photo) #фото карты
    bot.send_photo(message.chat.id, question[0][1]) # тут отправляем первое фото задания
    bot.send_message(message.chat.id, text = 'What checkpoint is this?')
    bot.register_next_step_handler(msg, process_one_question)


def process_one_question(message):
    try:
        user_id = message.chat.id
        user = User(message.text)
        user.user_id = user_id
        user_dict[user_id] = user
        bot.send_photo(user_id, question[1][1])
        # bot.send_message(user_id, text = user.answers)
        msg = bot.reply_to(message, text = 'What checkpoint is this?')
        bot.register_next_step_handler(msg, process_two_question)
    except Exception as e:
        bot.reply_to(message, '1oooops')


def process_two_question(message):
    # global User
    try:
        user_id = message.chat.id
        user = user_dict[user_id]
        user = user.append_answers(message.text)
        user_dict[user_id] = user
        msg = bot.reply_to(message, 'What checkpoint is this?')
        bot.send_photo(user_id, question[2][1])
        # bot.send_message(user_id, user.answers)
        bot.register_next_step_handler(msg, process_three_question)
    except Exception as e:
        bot.reply_to(message, '2oooops')


def process_three_question(message):
    try:
        user_id = message.chat.id
        # user = user_dict[user_id]
        # user.append_answers(message.text)
        # user_dict[user_id] = user
        bot.send_message(user_id, text = 'lol')
    except Exception as e:
        bot.reply_to(message, '3oooops')


@bot.message_handler(content_types=['text'])
def lol(message):
    global n
    count = 0
    user_id = message.chat.id
    user = user_dict[user_id]
    if message.text == 'результаты':
        for i in range(n):
            if user.answers[i] == question[i][2]:
                count += 1
        bot.send_message(message.chat.id, text = count )

bot.infinity_polling()