import pytest
from api.methods.courier_methods import delete_courier, login_courier
from helpers import register_new_courier_and_return_login_password


class TestLoginCourier:

    def test_login_courier(self):

        courier = register_new_courier_and_return_login_password()

        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        # авторизуемся
        r_login = login_courier(payload)
        assert r_login.status_code == 200 and r_login.json()["id"] is not None, f"Ошибка авторизации {r_login.text}"
        delete_courier(courier[0], courier[1])


    courier = register_new_courier_and_return_login_password()
    @pytest.mark.parametrize('login, password', [
        (courier[0], ''),
        ('', courier[1])
    ])
    def test_login_courier_missing_parameters(self, login, password):
        payload = {
            "login": login,
            "password": password
        }

        # авторизуемся с недостающими полями
        r_login = login_courier(payload)
        assert r_login.status_code == 400
        print(r_login.json()["message"])


    def test_login_non_existing_courier(self):

        courier = register_new_courier_and_return_login_password()

        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        delete_courier(courier[0], courier[1])

        # авторизуемся удаленным курьером
        r_login = login_courier(payload)
        assert r_login.status_code == 404
        print(r_login.json()["message"])

