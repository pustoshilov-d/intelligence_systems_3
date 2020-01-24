# -*- coding: utf-8 -*-
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random
import re

def parse(link, n):

    if (n<4):

            n = n + 1
            answer = vk.groups.getById(
                group_id = link[len("https://vk.com/"):],
                fields = "links")



            answer = answer[0]

            if(answer["name"] != "ИКБО-06-19 внутренняя"):
                print(link, " ",answer["name"])
                try:
                    for i in range(len(answer["links"])):
                        new_link = answer["links"][i]["url"]
                        if (re.match("https://vk.com/", new_link)):

                            parse(new_link, n)
                        else: print(new_link, " ", answer["links"][i]["name"])
                except KeyError: pass

vk_session = vk_api.VkApi(token='0f9aa49aeab766e682e9202badd3169ed08b66b01f9cc53bcf9c7481b635265cc8ca7d1b15b1b56bf91cb')
vk = vk_session.get_api()
mn = set()
parse("https://vk.com/sumirea", 0)
