import telebot
import config
from telebot import types
import time


token = '893243007:AAH9DnvnE8HvQYDuyM8B459ERu0s3RAPyns'
bot = telebot.TeleBot(token)


def invest(id):
	global my_list, n, sost, answers
	if config.n == 7:
		bot.send_message(id, my_list[config.n])
		s = ''
		for i in range(len(config.answers)):
			s += str(config.answers[i]) + '\n'
		bot.send_message('@dannie_iz_bota', s)
		sost = 0
	else:
		bot.send_message(id, my_list[config.n])

my_list = [
	'Регион приобретения объекта: ',
	'Стоимость объекта(До_____тыс.руб.):',
	'Срок сдачи объекта не позднее:',
	'Какие ещё пожелания?',
	'Ваш Email?',
	'Ваше Имя?',
	'Ваш номер телефона?',
	'Спасибо! Мы пришлём информацию вам на почту'
]


@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, 'Нажмите кнопку "Подобрать объект"', reply_markup=keyboard1())

def keyboard1():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Подобрать объект')
	markup.add(button_1)
	return markup


@bot.message_handler(content_types=['text'])
def handle_text(message):
	global my_list, n, sost, answers
	if message.text == 'Подобрать объект':
		bot.send_message(message.chat.id, 'Заполните краткую анкету: ')
		bot.send_message(message.chat.id, 'Для кого ведётся подбор?', reply_markup=keyboard2())
	elif message.text == 'Для себя':
		config.n = 0
		config.sost = 1
		config.answers = []
		config.answers.append(message.chat.username)
		config.answers.append('Для себя')
		bot.send_message(message.chat.id, 'Цель покупки недвижимости?', reply_markup=keyboard3())
	elif message.text == 'Я агент':
		config.n = 0
		config.sost = 1
		config.answers.append(message.chat.username)
		config.answers.append('Я агент')
		bot.send_message(message.chat.id, 'Цель покупки недвижимости?', reply_markup=keyboard3())
	elif message.text == 'Инвестиции':
		config.answers.append('Инвестиции')
		invest(message.chat.id)
	elif message.text == 'Проживание':
		config.answers.append('Проживание')
		invest(message.chat.id)
	else:
		if config.sost == 1:
			config.answers.append(message.text)
			config.n += 1
			invest(message.chat.id)


def keyboard2():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Для себя')
	button_2 = types.KeyboardButton('Я агент')
	markup.add(button_1)
	markup.add(button_2)
	return markup


def keyboard3():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Инвестиции')
	button_2 = types.KeyboardButton('Проживание')
	markup.add(button_1)
	markup.add(button_2)
	return markup


bot.polling(none_stop=True, interval=0)
