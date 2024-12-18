class Order:
    address = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
        }

class ErrorMessages:
    courier_create_409 = 'Этот логин уже используется. Попробуйте другой.'
    courier_create_400 = 'Недостаточно данных для создания учетной записи'
    courier_login_400 = 'Недостаточно данных для входа'
    courier_login_404 = 'Учетная запись не найдена'
