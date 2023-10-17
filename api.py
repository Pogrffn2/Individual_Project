from requests import Session

class JournalAPI:

    url = 'https://msapi.top-academy.ru/api/v2/' # URL для API колледжа
    app_id = '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6' # Обращение к сайту по appid

    def __init__(self, username, password):

        self.user = None
        self.all_homeworks = []
        self.username = username
        self.password = password
        self.sess = Session()
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