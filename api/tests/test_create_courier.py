import pytest
from api.methods.courier_methods import create_courier, delete_courier
from data import ErrorMessages
from helpers import register_new_courier_and_return_login_password, generate_new_courier_data


class TestCreateCourier:

    courier_data_1 = generate_new_courier_data()
    courier_data_2 = generate_new_courier_data()
    @pytest.mark.parametrize('login, password, first_name',[
        (courier_data_1[0], courier_data_1[1], courier_data_1[2]),
        (courier_data_2[0], courier_data_2[1], '')
    ])
    def test_create_new_courier(self, login, password, first_name):

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        #создаем курьера в системе
        r_create = create_courier(payload)
        assert r_create.status_code == 201 and r_create.json()["ok"] == True, f"Ошибка создания курьера"
        delete_courier(login, password)


    def test_create_the_same_courier(self):

        courier = register_new_courier_and_return_login_password()

        payload = {
            "login": courier[0],
            "password": courier[1],
            "firstName": courier[2]
        }

        r_create = create_courier(payload)
        assert r_create.status_code == 409 and r_create.json()["message"] == ErrorMessages.courier_create_409
        print(r_create.json()["message"])

        delete_courier(courier[0], courier[1])


    @pytest.mark.parametrize('login, password, first_name', [
        ('', courier_data_1[1], courier_data_1[2]),
        (courier_data_2[0], '', courier_data_2[2])
    ])
    def test_create_new_courier_missing_parameters(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # создаем курьера с недостающими полями
        r_create = create_courier(payload)
        assert r_create.status_code == 400 and r_create.json()["message"] == ErrorMessages.courier_create_400
        print(r_create.json()["message"])
