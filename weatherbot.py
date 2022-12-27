import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5441803313:AAFzXkVEkyThRFCBD1VppuvHR8JM6mynujE')

@bot.message_handler(comands = ['start'])
def hello(message):
    bot.send_message(message.chat.id, "Приветствую тебя, воин Азерота")

@bot.message_handler(comands = ['help'])
def hello(message):
    bot.send_message(message.chat.id, "Список команд")

@bot.message_handler(command_types = ['text'])
def test(message):
    try:
        config_dict = get_default_config()
        config_dict['language'] = 'ru'

        place = message.text

        owm = OWM('c52242b2d4d80ae028d6e97b46ce1c39', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']

        wi = w.wind()['speed']
        humi = w.humidity
        cl = w.clouds
        st = w.clouds
        dt = w.detailed_status
        ti = w.reference_time('iso')
        pr = w.pressure['press']
        vd = w.visibility_distance

        bot.send_message(message.chat.id, "В городе " + str(place) + "температура" + str(t1) + "C" + "\n" +
                         "Максимальная температура" + str(t3) + "C" + "\n" +
                         "Минимальная температура" + str(t4) + "C" + "\n" +
                         "Ощущается как" + str(t2) + "C" + "\n" +
                         "Скорость ветра" + str(pr) + "м/с" + "\n" +
                         "Давление" + str(pr) + "C" + "мм.рт.ст" +
                         "Влажность" + str(humi) + "%" + "\n" +
                         "Видимость" + str(vd) + "метров" + "\n" +
                         "Статус" + str(st) + "\n\n" + str(dt))



    except:
        bot.send_message(message.chat.id,"Такой город не найден!")
        print(str(message.text), "- не найден")

bot.polling(none_stop = True, interval=0)



