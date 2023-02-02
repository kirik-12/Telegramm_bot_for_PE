import telebot
from telebot import types
import foto as ft

token = '6072418722:AAFkuqO-wt9XlzF9_Z1btbAnIczV2Jx8Eyo'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Game 1")
    btn2 = types.KeyboardButton("Game 2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id , text = f'{message.from_user.first_name}, готов страдать?' )


    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Game 1"):
        bot.send_message(message.chat.id, text="Твой выбор сделан... ДА Начнётся игра!!!")
        bot.send_photo(message.shat.id, ft.map_photo)
    elif
   '''     
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
'''

bot.polling(non_stop=True)