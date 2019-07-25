import telebot
from telebot import types


token = '893243007:AAH9DnvnE8HvQYDuyM8B459ERu0s3RAPyns'
bot = telebot.TeleBot(token)


answers = []
sost = 0
n = 0
m = 0



def sending(id, message):
	global my_list, n, sost, answers
	if n == 8:
		bot.send_message(id,'Спасибо! Мы пришлём информацию вам на почту')
		answers.append('номер: ' + message.text)
		s = ''
		for i in range(len(answers)):
			s += str(answers[i]) + '\n'
		bot.send_message('@dannie_iz_bota', s)
		sost = 0
	elif n == 1:
		bot.send_message(id, 'Регион приобретения объекта: ')
	elif n == 2:
		bot.send_message(id, 'Стоимость объекта(До_____тыс.руб.): ')
		answers.append('регион: ' + message.text)
	elif n == 3:
		bot.send_message(id, 'Срок сдачи объекта не позднее: ')
		answers.append('стоимость: ' + message.text)
	elif n == 4:
		bot.send_message(id, 'Какие ещё пожелания?')
		answers.append('срок: ' + message.text)
	elif n == 5:
		bot.send_message(id, 'Ваш Email?')
		answers.append('пожелания: ' + message.text)
	elif n == 6:
		bot.send_message(id, 'Ваше Имя?')
		answers.append('email: ' + message.text)
	elif n == 7:
		bot.send_message(id, 'Ваш номер телефона?')
		answers.append('имя: ' + message.text)



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
		n = 0
		sost = 1
		answers = []
		answers.append('@' + message.chat.username)
		answers.append('для кого: Для себя')
		bot.send_message(message.chat.id, 'Цель покупки недвижимости?', reply_markup=keyboard3())
	elif message.text == 'Я агент':
		n = 0
		sost = 1
		answers = []
		answers.append('@' + message.chat.username)
		answers.append('для кого: Я агент')
		bot.send_message(message.chat.id, 'Цель покупки недвижимости?', reply_markup=keyboard3())
	elif message.text == 'Инвестиции':
		answers.append('цель: Инвестиции')
		n += 1
		sending(message.chat.id, message)
	elif message.text == 'Проживание':
		answers.append('цель: Проживание')
		n += 1
		sending(message.chat.id, message)
	else:
		if sost == 1:
			n += 1
			sending(message.chat.id, message)
			print(answers)


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
