# import telebot.types
# from api import JournalAPI
# from telebot.async_telebot import AsyncTeleBot
# import asyncio
import requests
#
# bot = telebot.TeleBot(token = '6548731888:AAFJH1hwf6_toOXWgTsR2saQFjnrSdA1Prk')
#

#
# @bot.message_handler(commands=['start'])
# async def start(message: telebot.types.Message):
#     await bot.send_message(message.chat.id, f'Привет, твой ID чата: {message.chat.id}')
#
# @bot.message_handler(commands=['hworks'])
# async def hworks(message: telebot.types.Message):
#     await bot.send_message(message.chat.id, f'{api.get_homeworks()}')
#     print(api.user)
#     print(api.all_homeworks)
#
# asyncio.run(bot.infinity_polling())

class JournalAPI:
    url = 'https://msapi.top-academy.ru/api/v2/' # URL для API колледжа
    app_id = '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6' # Обращение к сайту по appid

    def __init__(self, username, password):
        self.user = None
        self.all_homeworks = []
        self.username = username
        self.password = password
        self.sess = requests.Session()
        self.sess.headers['Authorization'] = 'Bearer null'

    def login(self):
        endpoint = 'auth/login'
        answ = self.sess.post(url=f'{self.url}{endpoint}',
                              json={
                                    'application_key': self.app_id,
                                    'id_city': None,
                                    'username': self.username,
                                    'password': self.password
                              })
        print(answ.status_code)
        if answ.status_code == 200: self.sess.headers['Authorization'] = f"Bearer {answ.json()['access_token']}"
        else: return False

    def get_info(self):
        if self.user is None:
            endpoint = 'settings/user-info'
            answ = self.sess.get(url=f'{self.url}{endpoint}')
            if answ.status_code == 200:
                self.user = answ.json()
                return self.user
            else:
                if not self.login(): return False
                else: self.get_info()
        else: return self.user

    def get_homeworks(self):
        all_hw = []
        endpoint = 'homework/operations/list?page=1&status=$STATUS&type=0&group_id=15'
        for i in range(6):
            answ = self.sess.get(url=f'{self.url}{endpoint.replace("$STATUS", str(i))}')
            if answ.status_code == 200:
                print(answ.json())
                all_hw.append(answ.json())
            else:
                if not self.login(): return False
                else: self.get_homeworks()
        self.all_homeworks = all_hw
        print(self.all_homeworks)
        return self.all_homeworks

# api = JournalAPI('Kurch_sb05', 'a926BXg1')
# # print(api.login())
# # api.get_info()
# # api.get_homeworks()

headers = {
    'authority': 'msapi.top-academy.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru_RU, ru',
    'authorization': 'Bearer null',
    'content-type': 'application/json',
    'origin': 'https://journal.top-academy.ru',
    'referer': 'https://journal.top-academy.ru/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

json_data = {
    'application_key': '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6',
    'id_city': None,
    'password': 'a926BXg1',
    'username': 'Kurch_sb05',
}


response = requests.post('https://msapi.top-academy.ru/api/v2/auth/login', headers=headers, json=json_data)
headers['authorization'] = f"Bearer {response.json()['access_token']}"

params = {
    'date_filter': '2023-10-04'
}
# try:
response = requests.get('https://msapi.top-academy.ru/api/v2/schedule/operations/get-month', params=params, headers=headers)

code = response.status_code
if code == 200:
    print(response.json())
elif code == 401:
    print("Время истекло")
    response = requests.post('https://msapi.top-academy.ru/api/v2/auth/login', headers=headers, json=json_data)
    headers['authorization'] = f"Bearer {response.json()['access_token']}"
elif code == 403:
    print("Что-то")








# sess.headers['Authorization'] = 'Bearer null'
#
# answ = sess.post('https://msapi.top-academy.ru/api/v2/auth/login', headers=headers, json=json_data)
# print(answ.status_code)
#
# sess.headers['Authorization'] = f"Bearer {answ.json()['access_token']}"















#
# import requests
#
# headers = {
#     'authority': 'msapi.top-academy.ru',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'ru_RU, ru',
#     'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvbXNhcGkuaXRzdGVwLm9yZyIsImlhdCI6MTY5ODc1NDIxMywiYXVkIjoxLCJleHAiOjE2OTg3NTc4MTMsImFwaUFwcGxpY2F0aW9uSWQiOjEsImFwaVVzZXJUeXBlSWQiOjEsInVzZXJJZCI6MjcwLCJpZENpdHkiOjQxMn0.STC9zhCXCSOaojc0G0IedtmyKPl9Cuqf7EKOffp02es',
#     'origin': 'https://journal.top-academy.ru',
#     'referer': 'https://journal.top-academy.ru/',
#     'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
# }
#
# params = {
#     'date_filter': '2023-10-04',
# }
#
# response = requests.get('https://msapi.top-academy.ru/api/v2/schedule/operations/get-month', params=params, headers=headers)
# print(response.status_code)
#
# print(len(response.json()))
#
# for i in response.json():
#     print(i)


#
# test = response.json()
#
# date = []
# dict = {}
# for i in test:
#     dict[i['date']] = i
#
# for i in dict:
#     date.append(i)
# date.sort()
#
# # for day in date: print(day)
# #
# # params = {'date_filter': date[0],}
# # requests.get('https://msapi.top-academy.ru/api/v2/schedule/operations/get-by-date', params=params, headers=headers)
#
#
# for cur_date in date:
#     params = {'date_filter': cur_date,}
#     response = requests.get('https://msapi.top-academy.ru/api/v2/schedule/operations/get-by-date', params=params, headers=headers)
#     for j in response.json():
#         print(j)
#     print('\n')




