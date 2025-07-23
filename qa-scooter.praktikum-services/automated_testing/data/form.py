from .data import get_tomorrow_day


class DataOrderForm:
    "Тестовые данные формы заказа самоката"
    class PageOne:
        first_name = "Арсений"
        last_name = "Турлапов"
        address = "Москва"
        station = "Митино"
        phone = "+79998887766"

    class PageTwo:
        date = get_tomorrow_day()
        rend_day = 'семеро суток'
        color = 'чёрный жемчуг'
        comment = "Тестовый коммент"

    @staticmethod
    def get_data():
        data = {}
        data['page_one'] = {
            "fname": DataOrderForm.PageOne.first_name,
            "lname": DataOrderForm.PageOne.last_name,
            "address": DataOrderForm.PageOne.address,
            "metro": DataOrderForm.PageOne.station,
            "phone": DataOrderForm.PageOne.phone
        }
        data['page_two'] = {
            "date": DataOrderForm.PageTwo.date,
            "rend_day": DataOrderForm.PageTwo.rend_day,
            "color": DataOrderForm.PageTwo.color,
            "comment": DataOrderForm.PageTwo.comment
        }
        return data

    @staticmethod
    def get_new_data():
        data = {}
        data['page_one'] = {
            "fname": "Иван",
            "lname": "Иванов",
            "address": "Москва, красная площадь",
            "metro": "Бибирево",
            "phone": "89998887766"
        }
        data['page_two'] = {
            "date": DataOrderForm.PageTwo.date,
            "rend_day": "трое суток",
            "color": "серая безысходность",
            "comment": DataOrderForm.PageTwo.comment
        }
        return data
