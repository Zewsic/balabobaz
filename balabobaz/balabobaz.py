import requests
from random import randint


def balaboba(text=str(randint(1, 4999999)), style=randint(0, 12), count=1):

    """
    :param text: входной текст для обработки
    :param style: стиль обработки:
        0 - Без стиля. По умолчанию.
        1 - Теории заговора.
        2 - ТВ-репортажи.
        3 - Тосты.
        4 - Пацанские цитаты.
        5 - Рекламные слоганы.
        6 - Короткие истории.
        7 - Подписи в Instagram.
        8 - Короче, Википедия.
        9 - Синопсисы фильмов.
        10 - Гороскоп.
        11 - Народные мудрости.
        12 - Балабоба x Garage.
    :param count: количество раз, которое текст будет обработан. (Относительная длинна итогового текста)
    :return: text: итоговый текст
    """

    for i in range(count):
        text = requests.get(f"http://zewsic.pythonanywhere.com/balaboba/{style}/{text}").text
    return text
