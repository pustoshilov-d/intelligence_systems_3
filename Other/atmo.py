import vk_api
import pandas as pd

vk_session = vk_api.VkApi(login='DimkaPusha@gmail.com', password='3dimkachDimkach')
vk_session.auth()
vk = vk_session.get_api()

data  = pd.read_csv('atmo.csv',  header=None)[:10]

print(data.shape)
#obj[1][0]
for obj in data.iterrows():
    message = "Привет! Ты заполнял Перепись «Атмосферы», но всё ещё не подключен к внутренней Рассылке отряда. Тыкни здесь «разрешить», чтобы получать оперативное и важное информирование для действующих вожатых: vk.cc/9ZAwcA"
    try:
        inf = vk.users.get (user_ids = obj[1][0],fields = 'sex')

        if inf[0]['sex'] == 2:
            message = inf[0]['first_name'] + ", привет! Ты заполнял Перепись «Атмосферы», но всё ещё не подключен к внутренней Рассылке отряда. Тыкни здесь «разрешить», чтобы получать оперативное и важное информирование для действующих вожатых: vk.cc/9ZAwcA"
        else:
            message = inf[0]['first_name'] + ", привет! Ты заполняла Перепись «Атмосферы», но всё ещё не подключена к внутренней Рассылке отряда. Тыкни здесь «разрешить», чтобы получать оперативное и важное информирование для действующих вожатых: vk.cc/9ZAwcA"

        print(inf)
    except: print(obj[1][0], ' не юзер')

    # try:
    print(vk.messages.send (peer_id = obj[1][0], message = message))

    # except:print(obj[1][0],' не сообщ')