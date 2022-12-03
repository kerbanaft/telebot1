import telebot
import speech_recognition as sr
import soundfile as sf
import requests


TOKEN = "5750069397:AAENaXxpo-Q87CLAxGgdiL0JGMMZaT6Hezw"
bot = telebot.TeleBot(TOKEN)
bot.delete_webhook()
r = sr.Recognizer()
@bot.message_handler(content_types=['voice'])
def trans(message):
    chat_id = message.chat.id
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    open("C:/kivy/voice.ogg",'wb').write(file.content)
    data, samplerate = sf.read('C:/kivy/voice.ogg','wb')
    sf.write("C:/kivy/new_voice.waw",'wb', data, samplerate)







bot.polling(none_stop=True)