import telebot
from telebot import types
import urllib
import convertapi
import os
from utils import convert

MyToken = "1152498547:AAEAt8_mt_Go02n68Y_DTl7SFNh88vb0prI"
convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
bot = telebot.TeleBot(MyToken)

@bot.message_handler(commands=['start'])
def handle_start(message):

    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    creator = types.KeyboardButton("Создатели")
    key.add(creator)

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJiC161x-iw0PGVIGvP4RuOotxE_HqfAAJMAgACUhThCrYN913wM4SvGQQ')
    bot.send_message(message.chat.id, 'Здравствуйте я бот от команды NNNL\
                                     \nОтправьте мне файл в формате PDF или DOCX\
                                     \nИнструкция: /help', reply_markup=key)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJiAV61xoXjbdkDCMGSJYk5QZDSoxonAAJZAANSFOEKVrNFzU2t1eYZBA')
    bot.send_message(message.chat.id, 'Загрузите файл в формате:\ndocx или pdf\n\nИнструкция: [ ](https://i.imgur.com/Pfch2bk.mp4)', parse_mode='markdown')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Создатели':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJiA161xqs9ZO_tPWEddW5aqxmGQPHpAAJdAANSFOEKt0XypYUoTswZBA')
        bot.send_message(message.chat.id, 'Данный телеграм бот был создан командой *NNNL* \n\
                                         \n**Проектный менеджер** - *Кузьмина Наталья*\
                                         \n**Аналитик** - *Зыков Никита*\
                                         \n**Программист** - *Попова Наталья*\
                                         \n**Тестировщик** - *Лещёва Елизавета*', parse_mode='markdown')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJiD161yP8mmqpBejIbQ4I7qpgGoaqQAAJpAANSFOEK3gyeeQ4j8DkZBA')
        bot.send_message(message.chat.id, 'Я умею только конвертировать!\n/help')

@bot.message_handler(content_types=["document"])
def convertDocToPDF(message):
    global convert_FILE
    global sticker
    global mess
    convert_FILE = message

    option = types.InlineKeyboardMarkup()
    pdf = types.InlineKeyboardButton(text='PDF ➜ DOCX', callback_data='pdf_to_word')
    docx = types.InlineKeyboardButton(text='DOCX ➜ PDF', callback_data='word_to_pdf')
    docx_to_png = types.InlineKeyboardButton(text='DOCX ➜ ФОТО', callback_data='word_to_png')
    pdf_to_png = types.InlineKeyboardButton(text='PDF ➜ ФОТО', callback_data='pdf_to_png')
    
    option.add(pdf, docx)
    option.add(docx_to_png, pdf_to_png)

    bot.delete_message(message.chat.id, message.message_id)
    sticker = bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJiDV61x_dqr30AAXPCbF38r0mZe5gkqgACMQADUhThCpsJWIQoEZeZGQQ')
    mess = bot.send_message(message.chat.id, "Выберити формат ковертации:", reply_markup=option)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'pdf_to_word':
        try:
            bot.delete_message(call.message.chat.id, sticker.message_id)
            bot.delete_message(call.message.chat.id, mess.message_id)
            sticker1 = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJiBV61xv7kcs4K5uZ5_h0fo8yRsirjAAJCAANSFOEK0lj9bqhpS5gZBA')
            message_send = bot.send_message(call.message.chat.id, "Конвертация...")
            
            imp = "pdf"
            exp = "docx"
            conv = "newFile." + imp
            
            con = convert_FILE
            fileID = con.document.file_id
            fileURL = bot.get_file_url(fileID)
            urllib.request.urlretrieve(fileURL, "newFile." + imp)
            
            fileToSend = convert(imp, exp, conv)
            bot.send_document(call.message.chat.id, fileToSend)
            
            os.remove("newFile." + imp)
            os.remove("convertedFile." + exp)
            
            bot.delete_message(call.message.chat.id, sticker1.message_id)
            bot.delete_message(call.message.chat.id, message_send.message_id)
        except:
            try:
                bot.delete_message(call.message.chat.id, sticker1.message_id)
                bot.delete_message(call.message.chat.id, message_send.message_id)
            except:
                print('Error')
            bot.send_message(call.message.chat.id, 'Ошибка! Неверный формат или файл поврежден!')
            
    elif call.data == 'word_to_pdf':
        try:
            bot.delete_message(call.message.chat.id, sticker.message_id)
            bot.delete_message(call.message.chat.id, mess.message_id)
            sticker1 = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJiBV61xv7kcs4K5uZ5_h0fo8yRsirjAAJCAANSFOEK0lj9bqhpS5gZBA')
            message_send = bot.send_message(call.message.chat.id, "Конвертация...")
            
            imp = "docx"
            exp = "pdf"
            conv = "newFile." + imp
            
            con = convert_FILE
            fileID = con.document.file_id
            fileURL = bot.get_file_url(fileID)
            urllib.request.urlretrieve(fileURL, "newFile." + imp)
            
            fileToSend = convert(imp, exp, conv)
            bot.send_document(call.message.chat.id, fileToSend)
            
            os.remove("newFile." + imp)
            os.remove("convertedFile." + exp)
            
            bot.delete_message(call.message.chat.id, sticker1.message_id)
            bot.delete_message(call.message.chat.id, message_send.message_id)
        except:
            try:
                bot.delete_message(call.message.chat.id, sticker1.message_id)
                bot.delete_message(call.message.chat.id, message_send.message_id)
            except:
                print('Error')
            bot.send_message(call.message.chat.id, 'Ошибка! Неверный формат или файл поврежден!')
            
    elif call.data == 'word_to_png':
        try:
            bot.delete_message(call.message.chat.id, sticker.message_id)
            bot.delete_message(call.message.chat.id, mess.message_id)
            sticker1 = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJiBV61xv7kcs4K5uZ5_h0fo8yRsirjAAJCAANSFOEK0lj9bqhpS5gZBA')
            message_send = bot.send_message(call.message.chat.id, "Конвертация...")
            
            imp = "docx"
            exp = "png"
            conv = "newFile." + imp
            
            con = convert_FILE
            fileID = con.document.file_id
            fileURL = bot.get_file_url(fileID)
            urllib.request.urlretrieve(fileURL, "newFile." + imp)
            
            fileToSend = convert(imp, exp, conv)
            bot.send_document(call.message.chat.id, fileToSend)
            
            os.remove("newFile." + imp)
            os.remove("convertedFile." + exp)
            
            bot.delete_message(call.message.chat.id, sticker1.message_id)
            bot.delete_message(call.message.chat.id, message_send.message_id)
        except:
            try:
                bot.delete_message(call.message.chat.id, sticker1.message_id)
                bot.delete_message(call.message.chat.id, message_send.message_id)
            except:
                print('Error')
            bot.send_message(call.message.chat.id, 'Ошибка! Неверный формат или файл поврежден!')
            
    elif call.data == 'pdf_to_png':
        try:
            bot.delete_message(call.message.chat.id, sticker.message_id)
            bot.delete_message(call.message.chat.id, mess.message_id)
            sticker1 = bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJiBV61xv7kcs4K5uZ5_h0fo8yRsirjAAJCAANSFOEK0lj9bqhpS5gZBA')
            message_send = bot.send_message(call.message.chat.id, "Конвертация...")
            
            imp = "pdf"
            exp = "png"
            conv = "newFile." + imp
            
            con = convert_FILE
            fileID = con.document.file_id
            fileURL = bot.get_file_url(fileID)
            urllib.request.urlretrieve(fileURL, "newFile." + imp)
            
            fileToSend = convert(imp, exp, conv)
            bot.send_document(call.message.chat.id, fileToSend)
            
            os.remove("newFile." + imp)
            os.remove("convertedFile." + exp)
            
            bot.delete_message(call.message.chat.id, sticker1.message_id)
            bot.delete_message(call.message.chat.id, message_send.message_id)
        except:
            try:
                bot.delete_message(call.message.chat.id, sticker1.message_id)
                bot.delete_message(call.message.chat.id, message_send.message_id)
            except:
                print('Error')
            bot.send_message(call.message.chat.id, 'Ошибка! Неверный формат или файл поврежден!')

bot.polling()