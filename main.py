import telebot 
from telebot import types
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup #States
from telebot.storage import StateMemoryStorage
import foto as ft
import random

# Now, you can pass storage to bot.
state_storage = StateMemoryStorage() # you can init here another storage
bot = telebot.TeleBot("6072418722:AAFkuqO-wt9XlzF9_Z1btbAnIczV2Jx8Eyo",
state_storage=state_storage)

# States group.
class Question(StatesGroup):
    que_1 = State()
    que_2 = State()
    que_3 = State()
    que_4 = State()
    que_5 = State()
    que_6 = State()
    que_7 = State()
    que_8 = State()
    que_9 = State()
    que_10 = State()
    que_11 = State()
    que_12 = State()
    que_13 = State()
    que_14 = State()
    que_15 = State()

# Здароваемся с нашей жертвой/ Даём кнопки 5,10,15 вопросов
@bot.message_handler(commands=['start'])
def start_ex(message):
    que_ft = ft.all_photos
    random.shuffle(que_ft)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!! не забудь изменить пятёрку на 15
    global question_foto_ans 
    question_foto_ans = que_ft[0:5]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/start_5'), types.KeyboardButton('10'), types.KeyboardButton('15'))
    bot.send_message(message.chat.id, 'Hi! Please, listen rules', reply_markup=markup)
    bot.send_photo(message.chat.id, ft.map_photo)

#'5'. Начало теста с 5ью вопросами
@bot.message_handler(commands=['start_5'])
def start_ex(message):
    bot.set_state(message.from_user.id, Question.que_1, message.chat.id)
    bot.send_photo(message.chat.id, question_foto_ans[0][1])
    bot.send_message(message.chat.id, text = '1. What is checkpoint?')

@bot.message_handler(state=Question.que_1)
def que_1_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[1][1])
    bot.send_message(message.chat.id, text = '2. What is checkpoint?')
    bot.set_state(message.from_user.id, Question.que_2, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_1'] = message.text
 
@bot.message_handler(state=Question.que_2)
def que_2_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[2][1])
    bot.send_message(message.chat.id, "3. What is checkpoint?")
    bot.set_state(message.from_user.id, Question.que_3, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_2'] = message.text

@bot.message_handler(state=Question.que_3)
def que_3_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[3][1])
    bot.send_message(message.chat.id, "4. What is checkpoint?")
    bot.set_state(message.from_user.id, Question.que_4, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_3'] = message.text

@bot.message_handler(state=Question.que_4)
def que_4_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[4][1])
    bot.send_message(message.chat.id, "5. What is checkpoint?")
    bot.set_state(message.from_user.id, Question.que_5, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_4'] = message.text

@bot.message_handler(state=Question.que_5)
def que_5_get(message):
    bot.send_message(message.chat.id, "Nice.Let`s look on you answer")
    bot.set_state(message.from_user.id, Question.que_6, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_5'] = message.text

 
# result
@bot.message_handler(state=Question.que_6)
def ready_for_answer(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Ready, take a look:\n<b>"
               f"1: {data['que_1']}\n"
               f"2: {data['que_2']}\n"
               f"3: {data['que_3']}\n"
               f"4: {data['que_4']}\n"
               f"5: {data['que_5']}</b>\n"
               'write: "mark", looking for you results  ')
        global results
        results = data
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(content_types=['text'])
def loli(message):
    if message.text == 'mark':
        count = 0
        for i in range(len(list(results.values()))):
            if question_foto_ans[i][2] == int(list(results.values())[i]): 
                count+=1
        bot.send_message(message.chat.id, text = f'результаты: {(count/len(results)) * 100}%')


#incorrect number
@bot.message_handler(state=Question, is_digit=False)
def age_incorrect(message):
    bot.send_message(message.chat.id, 'Please enter a number')

# register filters

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)