#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random

def main():
        #Токен из настроек группы
        vk_session = vk_api.VkApi(token='0f9aa49aeab766e682e9202badd3169ed08b66b01f9cc53bcf9c7481b635265cc8ca7d1b15b1b56bf91cb')
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, '185942564')

        vk.messages.send(  # Отправляем в чат без всяких упоминаний
            peer_id=2000000002,
            random_id=random.getrandbits(32),
            message='А можно и так'
        )

        for event in longpoll.listen(): #отправляем в чат по упоминанию
            print(event.obj) # выводит все события, связанные с группой
            print(event)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.text == '[club185942564|@ikbo0619]':

                    if event.from_user:  # Если написали в ЛС
                        vk.messages.send(  # Отправляем сообщение
                            user_id=event.obj.from_id,
                            random_id=random.getrandbits(32),
                            message='Ваш текст'
                        )
                    elif event.from_chat:  # Если написали в Беседе
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=random.getrandbits(32),
                            message='Вау'
                        )

if __name__ == '__main__':
    main()