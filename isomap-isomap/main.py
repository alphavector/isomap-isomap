import telebot
import googlemaps

import time
import json

TOKEN = '470785962:AAFvQasjawVNNkC0lSsv98B54RC-3fMGIOc'  # get token from command-line
MAPS_KEY = 'AIzaSyDTwPj1UDZ3ghD0qz7cfN-FMgOoJMnby_8'

if __name__ == "__main__":
    bot = telebot.TeleBot(TOKEN)
    gmaps = googlemaps.Client(key=MAPS_KEY)
    user_location = None
    full_address = None

    @bot.message_handler(commands=['start'])
    def process_start(message):
        bot.send_message(message.chat.id, "БИЧАРА, ПРИВЕТ!")

    @bot.message_handler(commands=['from_address'])
    def address_process(message):
        try:
            address = message.text.replace('/from_address ', '')
            gmaps_resp = gmaps.geocode(address)
            full_address = gmaps_resp[0]['formatted_address']
            user_location = gmaps_resp[0]['geometry']['location']
        except Exception:
            bot.send_message(message.chat.id, "Please, input correct address.")

    @bot.message_handler(content_types=['location'])
    def location_process(message):
        user_location = {'lat': message.location.latitude, 'lng': message.location.longitude}
        gmaps_resp = gmaps.reverse_geocode(user_location)
        full_address = gmaps_resp[0]['formatted_address']
        bot.send(message.chat.id, "БИЧАРА ТЫ!")

    @bot.message_handler()
    def text_process(message):
        try:
            import isochrone

            address = message.text
            gmaps_resp = gmaps.geocode(address)
            print('goof')
            full_address = gmaps_resp[0]['formatted_address']
            user_location = gmaps_resp[0]['geometry']['location']
            isochrone, filename = isochrone.generate_isochrone_map(full_address, 10)
            bot.send_message(message.chat.id, "http://storage.eos.com")
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Please, input correct address or command.")


    bot.polling()

#
# origin ="Donetske Highway, 9, Dnipropetrovs'k, Dnipropetrovsk Oblast, Ukraine, 49000"
# duration = 10
#
# isochrone = isochrone.generate_isochrone_map(origin, duration)
# print(isochrone)
