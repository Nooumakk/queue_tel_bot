from tele_bot.middleware import _


response_en_monitoring = {
    "Ваш транспорт {} в очереди": "Your transport {} is in the queue",
    "Вас вызвали в пункт пропуска": "You have been called to the checkpoint",
    "Вы больше не состоите в очереди": "You are no longer in line",
    "Ваш транспорт аннулирован": "Your transport has been cancelled.",
    "Бенякони": "Benyakoni",
    "Берестовица": "Berestovitsa",
    "Брест БТС": "Brest",
    "Григоровщина": "Grigorovshchina",
    "Каменный Лог": "Kamenny Log",
    "Котловка": "Kotlovka",
    "Урбаны": "Urbany",
    "Вызван в ПП": "Summoned to the checkpoint",
    "Аннулирован": "Canceled",
}
response_pl_monitoring = {
    "Ваш транспорт {} в очереди": "Twój transport {} w kolejce",
    "Вас вызвали в пункт пропуска": "Zostałeś wyzwany do granicy",
    "Вы больше не состоите в очереди": "Nie jesteś już w kolejce",
    "Ваш транспорт аннулирован": "Twój transport został anulowany",
    "Бенякони": "Bieniakoni",
    "Берестовица": "Berestowica",
    "Брест БТС": "Brest",
    "Григоровщина": "Grigorowszczina",
    "Каменный Лог": "Kamenny Log",
    "Котловка": "Kotlowka",
    "Урбаны": "Urbany",
    "Вызван в ПП": "Wyzwany do granicy",
    "Аннулирован": "Anulowany",
}


def _m(message, lang_code):
    if lang_code == "ru":
        return message
    elif lang_code == "en":
        return response_en_monitoring[message]
    else:
        return response_pl_monitoring[message]


def _k(text, lang_code):
    if lang_code == "ru":
        return text
    elif lang_code == "en":
        return "Main menu"
    else:
        return "Menu główne"


def srart_template():
    return _(
        "Здесь ты можешь узнать информацию об очереди на границе в зонах ожидания(ЗО)"
    )


def help_template():
    return _(
        "Бот списывает информацию с официально сайта рб - "
        "<i>https://mon.declarant.by/</i> и не"
        "является официальным, а лишь любительским."
        "Задача данного бота - отслеживать очередь зоны ожидания на основных пунктах пропуска РБ, и сообщать информацию о состоянии очереди пользователю."
        "Информацию можно получить по всем доступным для пересечения границы видом транспорта. "
        "Бот позволяет сохранять номера ваших т/с и использовать их в будущем, без необходимости постоянно вводить данные при проверке."
        "У каждого пользователя имеется свой личный кабинет, где он сам управляет своим аккаунтом, в частности"
        "номерами своих т/с.\n"
        "<b>Внимание! Информация о очереди содержит в себе транспорт из зоны ожидания без учета живой очереди на въезде в зону ожидания.</b>"
    )


def tiket_template():
    return _(
        """
Для отправки сообщения об ошибке, будь-то неверная информация или отсутствие ответа от бота,
перейдите по кнопке в чат поддержки, опишите всю ситуацию(желательно приложив скриншот), укажите в каком
именно месте у вас возникла ошибка (пункт пропуска/транспорт).
Ваше сообщение будет рассмотрено в ближайшее время, а ошибка исправлена.
"""
    )


def monitoring_template():
    return _(
        "Бот сканирует зоны ожидания и ищет в них ваш транспорт, чтобы в последующем следить и сообщать пользователю об движении в очереди"
    )
