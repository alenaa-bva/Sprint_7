import requests

def create_order(payload):
    r_order = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
    return r_order

def put_order(order_id, courier_id):
    r_order = requests.put(f'https://qa-scooter.praktikum-services.ru/v1/orders/accept/{order_id}?courierId={courier_id}')
    return r_order

def get_order_list_for_courier(courier_id):
    r_order = requests.get(f'https://qa-scooter.praktikum-services.ru/v1/orders?courierId={courier_id}')
    return r_order
