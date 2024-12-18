import requests

def create_courier(payload):
    r_create = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)
    return r_create


def login_courier(payload):
    r_login = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    return r_login


def delete_courier(login, password):

    payload = {
        "login": login,
        "password": password
    }

    # авторизуемся, чтобы узнать id курьера
    r_login = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    courier_id = r_login.json().get("id")

    # удаляем курьера
    r_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}', data=payload)
    return r_delete