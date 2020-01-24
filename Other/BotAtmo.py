#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random

def main():
        #Токен из настроек группы
        vk_session = vk_api.VkApi(token='2aea74f7da3a95a129ccf43674f281b3583b70b47de3f03e94fb13f410eee18f5983f820c2a4a0ae574a5')
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, '186961965')

        chat_users = [21048329, 170378262, 132108322, 4013183, 52167654, 144764574, 11068736, 73841504, 39424087, 101175255]
        for event in longpoll.listen(): #отправляем в чат по упоминанию
            print(event.obj) # выводит все события, связанные с группой
            print(event)
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.text == '[club186961965|@alko_prof_union], у кого сосать сегодня?':
                    if event.from_chat:
                        # Если написали в Беседе

                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=random.getrandbits(32),
                            message='Соси у @id'+ str(chat_users[random.randint(0, len(chat_users))-1])
                        )

'''   vk.messages.send(  # Отправляем в чат без всяких упоминаний
            peer_id=2000000001,
            random_id=random.getrandbits(32),
            message='А можно и так'
)'''


if __name__ == '__main__':
    main()