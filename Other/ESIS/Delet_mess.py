#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random

def main():
        #Токен из настроек группы
        vk_session = vk_api.VkApi(token='4137897779030a1b57fa416e94044eb856097c794dca789d21fb3d6766c82bb70864c9d23f1ecfdc7b690')
        vk = vk_session.get_api()
        l_limit = int(input("Введите левую границу сообщений: "))
        r_limit = int(input("Введите правую границу сообщений: "))
        for i in range(l_limit,r_limit):
            l = ""
            for j in range(100):
                l = str(i*100+j) + ", " + l
            res= vk.messages.getById(
                message_ids = l,
                group_id = 42869722)

            num = 0; l = ""
            for j in range(res['count']):
                if((res['items'][j]['text'][:40].find("спасибо за заполнение") != -1) or (res['items'][j]['text'][:2].find("#") != -1) or (res['items'][j]['text'][:40].find("Ваш уровень") != -1) or (res['items'][j]['text'][:40].find("Спасибо за прохождение") != -1)  ):
                    l = str(res['items'][j]['id']) + ", " + l
                    num = num + 1
            res2 = ""
            if (len(l)>0):
                res2 = vk.messages.delete(
                    message_ids = l,
                    group_id = 42869722
                )
            print(str(num) + " id's: " + l)


if __name__ == '__main__':
    main()