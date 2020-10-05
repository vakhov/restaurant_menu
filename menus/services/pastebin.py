import requests


class Pastebin:
    """Класс для создания записи в сервисе Pastebin и получение ссылки на эту запись"""

    def __init__(self, dev_key: str, username: str, password: str) -> None:
        self.dev_key: str = dev_key
        self.username: str = username
        self.password: str = password

    @property
    def _login_data(self) -> dict:
        """Данные для авторизации"""
        login_data = {
            'api_dev_key': self.dev_key,
            'api_user_name': self.username,
            'api_user_password': self.password
        }
        return login_data

    def _get_user_key(self) -> str:
        """Получение токена авторизации"""
        api_login = requests.post('https://pastebin.com/api/api_login.php', data=self._login_data)
        api_login.raise_for_status()
        return api_login.text

    def create_paste(self, text: str, title: str = 'title') -> str:
        """Создать запись в сервисе Pastebin"""
        data = {
            'api_dev_key': self.dev_key,
            'api_user_key': self._get_user_key(),
            'api_option': 'paste',
            'api_paste_code': text,
            'api_paste_private': 0,  # запись доступна всем
            'api_paste_name': title,
            'api_paste_expire_data': '1H',  # 1 час
            'api_paste_format': 'text'
        }
        api_post = requests.post('https://pastebin.com/api/api_post.php', data=data)
        api_post.raise_for_status()
        return api_post.text
