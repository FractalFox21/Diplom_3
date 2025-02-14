import requests
from data.handles import URL_REGISTER,  URL_ORDER
from data.URLS import URL_HOME_PAGE


class Queries:

    #метод для создания API пользователя
    @staticmethod
    def post_create_user(data=None):
        url = f"{URL_HOME_PAGE}{URL_REGISTER}"
        response = requests.post(url, json=data)
        return response

    # метод для создания API заказа и получения его номера
    @staticmethod
    def post_create_order(data=None, token=None):
        url = f"{URL_HOME_PAGE}{URL_ORDER}"
        response = requests.post(url, json=data,  headers={'Authorization': f'{token}'})
        data = response.json()
        return data["order"]["number"]
