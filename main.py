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
class Question_5(StatesGroup):
    que_1 = State()
    que_2 = State()
    que_3 = State()
    que_4 = State()
    que_5 = State()
    result_5 = State()

class Question_10(StatesGroup):
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
    result_10 = State()

class Question_15(StatesGroup):
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
    result_15 = State()



# Здароваемся с нашей жертвой/ Даём кнопки 5,10,15 вопросов
@bot.message_handler(commands=['start'])
def start_ex(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/start_5'), types.KeyboardButton('/start_10'), types.KeyboardButton('/start_15'))
    bot.send_message(message.chat.id, 'Hi! Please, listen rules', reply_markup=markup)
    bot.send_photo(message.chat.id, ft.map_photo)



#'5'. Начало теста с 5ью вопросами
@bot.message_handler(commands=['start_5'])
def start_ex(message):
    que_ft = ft.all_photos
    random.shuffle(que_ft)
    global question_foto_ans 
    question_foto_ans = que_ft[0:5]
    a = telebot.types.ReplyKeyboardRemove()
    bot.set_state(message.from_user.id, Question_5.que_1, message.chat.id)
    bot.send_photo(message.chat.id, question_foto_ans[0][1])
    bot.send_message(message.chat.id, text = '1. What is checkpoint?', reply_markup=a)

@bot.message_handler(state=Question_5.que_1)
def que_1_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[1][1])
    bot.send_message(message.chat.id, text = '2. What is checkpoint?')
    bot.set_state(message.from_user.id, Question_5.que_2, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_1'] = message.text
 
@bot.message_handler(state=Question_5.que_2)
def que_2_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[2][1])
    bot.send_message(message.chat.id, "3. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_5.que_3, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_2'] = message.text

@bot.message_handler(state=Question_5.que_3)
def que_3_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[3][1])
    bot.send_message(message.chat.id, "4. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_5.que_4, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_3'] = message.text

@bot.message_handler(state=Question_5.que_4)
def que_4_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[4][1])
    bot.send_message(message.chat.id, "5. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_5.que_5, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_4'] = message.text

@bot.message_handler(state=Question_5.que_5)
def que_5_get(message):
    bot.send_message(message.chat.id, "Nice. Let`s look on you answer!")
    bot.send_message(message.chat.id, 'Write anything...')
    bot.set_state(message.from_user.id, Question_5.result_5, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_5'] = message.text

# result
@bot.message_handler(state=Question_5.result_5)
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



#'10'. Начало теста с 10ью вопросами 
@bot.message_handler(commands=['start_10'])
def start_ex_10(message):
    que_ft = ft.all_photos
    random.shuffle(que_ft)
    global question_foto_ans 
    question_foto_ans = que_ft[0:10]
    a = telebot.types.ReplyKeyboardRemove()
    bot.set_state(message.from_user.id, Question_10.que_1, message.chat.id)
    bot.send_photo(message.chat.id, question_foto_ans[0][1])
    bot.send_message(message.chat.id, text = '1. What is checkpoint?', reply_markup=a)

@bot.message_handler(state=Question_10.que_1)
def que_1_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[1][1])
    bot.send_message(message.chat.id, text = '2. What is checkpoint?')
    bot.set_state(message.from_user.id, Question_10.que_2, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_1'] = message.text
 
@bot.message_handler(state=Question_10.que_2)
def que_2_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[2][1])
    bot.send_message(message.chat.id, "3. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_3, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_2'] = message.text

@bot.message_handler(state=Question_10.que_3)
def que_3_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[3][1])
    bot.send_message(message.chat.id, "4. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_4, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_3'] = message.text

@bot.message_handler(state=Question_10.que_4)
def que_4_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[4][1])
    bot.send_message(message.chat.id, "5. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_5, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_4'] = message.text

@bot.message_handler(state=Question_10.que_5)
def que_5_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[5][1])
    bot.send_message(message.chat.id, "6. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_6, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_5'] = message.text

@bot.message_handler(state=Question_10.que_6)
def que_6_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[6][1])
    bot.send_message(message.chat.id, "7. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_7, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_6'] = message.text

@bot.message_handler(state=Question_10.que_7)
def que_7_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[7][1])
    bot.send_message(message.chat.id, "8. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_8, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_7'] = message.text

@bot.message_handler(state=Question_10.que_8)
def que_8_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[8][1])
    bot.send_message(message.chat.id, "9. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_9, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_8'] = message.text

@bot.message_handler(state=Question_10.que_9)
def que_9_get_10(message):
    bot.send_photo(message.chat.id, question_foto_ans[9][1])
    bot.send_message(message.chat.id, "10. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_10.que_10, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_9'] = message.text

@bot.message_handler(state=Question_10.que_10)
def que_10_get_10(message):
    bot.send_message(message.chat.id, "Nice. Let`s look on you answer!")
    bot.send_message(message.chat.id, 'Write anything...')
    bot.set_state(message.from_user.id, Question_10.result_10, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_10'] = message.text

# result
@bot.message_handler(state=Question_10.result_10)
def ready_for_answer(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Ready, take a look:\n<b>"
               f"1: {data['que_1']}\n"
               f"2: {data['que_2']}\n"
               f"3: {data['que_3']}\n"
               f"4: {data['que_4']}\n"
               f"5: {data['que_5']}\n"
               f"6: {data['que_6']}\n"
               f"7: {data['que_7']}\n"
               f"8: {data['que_8']}\n"
               f"9: {data['que_9']}\n"
               f"10: {data['que_10']}</b>\n"
               'Write: "mark", looking for you results')
        global results
        results = data
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)




#'15'. Начало теста с 15ью вопросами 
@bot.message_handler(commands=['start_15'])
def start_ex(message):
    que_ft = ft.all_photos
    random.shuffle(que_ft)
    global question_foto_ans 
    question_foto_ans = que_ft[0:15]
    a = telebot.types.ReplyKeyboardRemove()
    bot.set_state(message.from_user.id, Question_15.que_1, message.chat.id)
    bot.send_photo(message.chat.id, question_foto_ans[0][1])
    bot.send_message(message.chat.id, text = '1. What is checkpoint?', reply_markup=a)

@bot.message_handler(state=Question_15.que_1)
def que_1_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[1][1])
    bot.send_message(message.chat.id, text = '2. What is checkpoint?')
    bot.set_state(message.from_user.id, Question_15.que_2, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_1'] = message.text
 
@bot.message_handler(state=Question_15.que_2)
def que_2_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[2][1])
    bot.send_message(message.chat.id, "3. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_3, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_2'] = message.text

@bot.message_handler(state=Question_15.que_3)
def que_3_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[3][1])
    bot.send_message(message.chat.id, "4. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_4, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_3'] = message.text

@bot.message_handler(state=Question_15.que_4)
def que_4_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[4][1])
    bot.send_message(message.chat.id, "5. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_5, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_4'] = message.text

@bot.message_handler(state=Question_15.que_5)
def que_5_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[5][1])
    bot.send_message(message.chat.id, "6. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_6, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_5'] = message.text

@bot.message_handler(state=Question_15.que_6)
def que_6_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[6][1])
    bot.send_message(message.chat.id, "7. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_7, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_6'] = message.text

@bot.message_handler(state=Question_15.que_7)
def que_7_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[7][1])
    bot.send_message(message.chat.id, "8. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_8, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_7'] = message.text

@bot.message_handler(state=Question_15.que_8)
def que_8_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[8][1])
    bot.send_message(message.chat.id, "9. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_9, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_8'] = message.text

@bot.message_handler(state=Question_15.que_9)
def que_9_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[9][1])
    bot.send_message(message.chat.id, "10. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_10, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_9'] = message.text

@bot.message_handler(state=Question_15.que_10)
def que_10_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[10][1])
    bot.send_message(message.chat.id, "11. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_11, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_10'] = message.text

@bot.message_handler(state=Question_15.que_11)
def que_11_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[11][1])
    bot.send_message(message.chat.id, "12. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_12, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_11'] = message.text

@bot.message_handler(state=Question_15.que_12)
def que_12_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[12][1])
    bot.send_message(message.chat.id, "13. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_13, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_12'] = message.text

@bot.message_handler(state=Question_15.que_13)
def que_13_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[13][1])
    bot.send_message(message.chat.id, "14. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_14, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_13'] = message.text

@bot.message_handler(state=Question_15.que_14)
def que_14_get(message):
    bot.send_photo(message.chat.id, question_foto_ans[14][1])
    bot.send_message(message.chat.id, "15. What is checkpoint?")
    bot.set_state(message.from_user.id, Question_15.que_15, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_14'] = message.text

@bot.message_handler(state=Question_15.que_15)
def que_15_get(message):
    bot.send_message(message.chat.id, "Nice. Let`s look on you answer!")
    bot.send_message(message.chat.id, 'Write anything...')
    bot.set_state(message.from_user.id, Question_15.result_15, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['que_15'] = message.text

# result
@bot.message_handler(state=Question_15.result_15)
def ready_for_answer(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Ready, take a look:\n<b>"
               f"1: {data['que_1']}\n"
               f"2: {data['que_2']}\n"
               f"3: {data['que_3']}\n"
               f"4: {data['que_4']}\n"
               f"5: {data['que_5']}\n"
               f"6: {data['que_6']}\n"
               f"7: {data['que_7']}\n"
               f"8: {data['que_8']}\n"
               f"9: {data['que_9']}\n"
               f"10: {data['que_10']}\n"
               f"11: {data['que_11']}\n"
               f"12: {data['que_12']}\n"
               f"13: {data['que_13']}\n"
               f"14: {data['que_14']}\n"
               f"15: {data['que_15']}</b>\n"
               'Write: "mark", looking for you results')
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
        bot.send_message(message.chat.id, text = f'результаты: {round(count/len(results)) * 100}%')


#incorrect number
@bot.message_handler(state=Question_5, is_digit=False)
def age_incorrect(message):
    bot.send_message(message.chat.id, 'Please enter a number')


# register filters
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)