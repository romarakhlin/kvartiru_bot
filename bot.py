import telebot
import config
from telebot import types
import requests


token = '655758905:AAHW9Raxw0tQUVeN8PKaXRgIlMh5LqmeJGY'
bot = telebot.TeleBot(token)


def bitok(id):
    global listbit, n1, sost1, answers1
    if config.n1 == 3:
        bot.send_message(id, listbit[config.n1])
        s = ''
        for i in range(len(config.answers1)):
            s += str(config.answers1[i]) + '\n'
        bot.send_message('@rulechannell', s)
    else:
        bot.send_message(id, listbit[config.n1])
 
def exmo(id):
    global listexmo, n2, sos2, answers2
    if config.n2 == 2:
        bot.send_message(id, listexmo[config.n2])
        s = ''
        for i in range(len(config.answers2)):
            s += str(config.answers2[i]) + '\n'
        bot.send_message('@rulechannell', s)
    else:
        bot.send_message(id, listexmo[config.n2])

listbit = [
    'На какую сумму в RUB вы собираетесь приобретать BTC?',
    '🔴 Чтобы продолжить заполнять заявку вы должны согласиться с указанными нижк правилами \n\n❗ Не хамите и не грубите операторам заявок ❗\n❗ Выполняйте все строго по инструкции ❗\n❗ При не соблюдении данных правил - оператор имеет право отказатся от дальнейшего с вами общения ❗\n\nНапишите "Понятно" для продолжения заполнения заявки.',
    'Укажите свой BTC кошелек: ',
    '🔴 В течении 10 мин с вами свяжется оператор \nОператор проверит указанные вами данные и выставит платеж \n\n Ожидайте сообщение оператора!!!'
]

listexmo = [
    'На какую сумму в RUB вы собираетесь приобретать EXMO RUB?',
    '🔴 Чтобы продолжить заполнять заявку вы должны согласиться с указанными нижк правилами \n\n❗ Не хамите и не грубите операторам заявок ❗\n❗ Выполняйте все строго по инструкции ❗\n❗ При не соблюдении данных правил - оператор имеет право отказатся от дальнейшего с вами общения ❗\n\nНапишите "Понятно" для продолжения заполнения заявки.',
    '🔴 В течении 10 мин с вами свяжется оператор \nОператор проверит указанные вами данные и выставит платеж \n\n Ожидайте сообщение оператора!!!'
]


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard1())
 
 
def keyboard1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('Купить криптовалюту')
    button_2 = types.KeyboardButton('Поддержка')
    markup.add(button_1)
    markup.add(button_2)
    return markup
 
 
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Поддержка':
        bot.send_message(message.chat.id, 'ТЕХ ПОДДЕРЖКА ' + '\n\nпо всем вопросам: ')
    elif message.text == 'Купить криптовалюту':
        bot.send_message(message.chat.id, 'Выберите криптовалюту: ', reply_markup=keyboard2())
    elif message.text == 'Bitcoin (BTC)':
        config.n1 = 0
        config.sost1 = 1
        config.answers1.append('от: ' + '@' + message.chat.username)
        config.answers1.append('хочет: ' + 'BTC')
        bitok(message.chat.id)
    elif config.sost1 == 1:
        config.m1 += 1
        config.answers1.append(config.lis1[config.m1] + message.text)
        config.n1 += 1
        bitok(message.chat.id)
    elif message.text == 'Exmo RUB':
        config.n2 = 0
        config.sost2 = 1
        config.answers2.append('от: ' + '@' + message.chat.username)
        config.answers2.append('хочет: ' + 'EXMO RUB')
        exmo(message.chat.id)
    elif config.sost2 == 1:
        config.m2 += 1
        config.answers2.append(config.lis2[config.m2] + message.text)
        config.n2 += 1
        exmo(message.chat.id)
    elif config.sost1 == 4:
        bot.send_message(message.chat.id, 'Что дальше?', reply_markup=keyboard4())
    elif config.sost2 == 3:
        bot.send_message(message.chat.id, 'Что дальше?', reply_markup=keyboard4())

def keyboard2():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('Bitcoin (BTC)')
    button_2 = types.KeyboardButton('Exmo RUB')
    markup.add(button_1)
    markup.add(button_2)
    return markup

def keyboard3():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('Назад в меню')
    markup.add(button_1)
    return markup

def keyboard2():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('Продожить покупки')
    button_2 = types.KeyboardButton('На сегодня все')
    markup.add(button_1)
    markup.add(button_2)
    return markup


bot.polling(none_stop=True, interval=0)
