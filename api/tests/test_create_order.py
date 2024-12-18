import pytest
from api.methods.courier_methods import login_courier
from api.methods.order_methods import create_order, put_order, get_order_list_for_courier
from data import Order
from helpers import register_new_courier_and_return_login_password


class TestCreateOrder:

    @pytest.mark.parametrize('color_1, color_2', [
        ('BLACK', ''),
        ('', 'GREY'),
        ('BLACK', 'GREY'),
        ('', '')
    ])
    def test_create_order(self, color_1, color_2):
        Order.address["color"].append(color_1)
        Order.address["color"].append(color_2)
        payload = Order.address

        # создаем заказ
        r_order = create_order(payload)
        assert r_order.status_code == 201 and r_order.json()["track"] is not None, f"Ошибка создания заказа"


    def test_get_order_list(self):

        # создаем курьера
        courier = register_new_courier_and_return_login_password()
        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        # авторизуемся, чтобы узнать id
        r_login = login_courier(payload)
        courier_id = r_login.json().get("id")

        # размещаем заказ
        payload = Order.address
        r_order = create_order(payload)
        order_id = r_order.json().get('track')

        # назначаем курьера на заказ
        put_order(order_id, courier_id)

        # получаем список заказов курьера
        r_order_list = get_order_list_for_courier(courier_id)

        assert r_order_list.status_code == 200, f"Ошибка получения списка заказов курьера"


