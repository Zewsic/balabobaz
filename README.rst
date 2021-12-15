TempMailz
=========

Модуль для Python для взаимодействия с Балабобой(https://yandex.ru/lab/yalm).

Требования
------------

`requests <https://crate.io/packages/requests/>`_ - обязателен.

Установка
------------

Установка через PIP::

    $ pip install balabobaz

Использование
-----

Модернизация случайного текста со случайным стилем::

    from balabobaz import balabobaz as bb
    
    print(bb.balaboba())

Модернизация необходимого текста со случайным стилем::

    from balabobaz import balabobaz as bb
    
    print(bb.balaboba(text="Антон сегодня был злой."))

Модернизация необходимого текста со необходимым стилем::

    from balabobaz import balabobaz as bb
    
    print(bb.balaboba(text="Антон сегодня был злой.", style=6))
    
Модернизация необходимого текста со необходимым стилем и с указанием длинны::

    from balabobaz import balabobaz as bb
    
    print(bb.balaboba(text="Антон сегодня был злой.", style=6, count=3))
